#!/usr/bin/env python3
"""
running_shoe_model.py  -  ECM3175 Individual Project, preliminary work
======================================================================

WHAT THIS DOES
--------------
Two small impact models that use the SAME shoe-foam law:

  A) SHOE TEST RIG  (ASTM F1976-style drop test)
     An 8.5 kg striker is dropped onto the heel of the shoe with 5 J of
     energy (drop height ~60 mm). The model predicts the peak deceleration
     (g), peak force (N), foam compression (mm) and energy return that your
     rig would measure for new, worn and different foams.
     -> tells you what load cell / accelerometer range and sampling rate
        you need, and what differences you should expect to detect.

  B) RUNNER HEEL STRIKE  ("effective mass" impact)
     At heel strike part of the body (foot + shank, here 8% of body mass)
     stops suddenly on the heel pad + shoe. The model predicts the impact
     transient: peak force (in body weights, BW) and loading rate (BW/s),
     for different shoe stiffness, body masses, and new vs worn foam.

THE FOAM LAW (used for both the shoe and the heel pad)
------------------------------------------------------
    F(x) = k0 * x / (1 - x / x_max)          (x = compression)

    k0     initial stiffness [N/m]
    x_max  compression at which the foam is fully crushed (densified) [m]
           -> force shoots up as x approaches x_max ("bottoming out")
Damping: Hunt-Crossley,  F_total = F(x) * (1 + beta * x_dot)
The heel pad and the shoe midsole act in series (forces equal,
compressions add).

HOW TO RUN
----------
    python running_shoe_model.py          figures -> ../figures/

IMPORTANT
---------
Simplified, illustrative model. Shoe stiffness values come from a published
trial (soft 61 N/mm, hard 95 N/mm: Malisoux et al. 2020). Everything marked
ASSUMPTION (heel pad, worn-foam changes, energy return) must be replaced by
your own drop-test measurements if you choose this project.
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

G = 9.81
FIG_DIR = Path(__file__).resolve().parent.parent / "figures"

# --- Shoes (heel region) --------------------------------------------------
# k0 from Malisoux et al. (2020), Am J Sports Med 48(2):473-480:
# soft prototype 61.3 N/mm, hard prototype 94.9 N/mm.
SHOES = {
    "Soft, new":      dict(k0=61e3, x_max=0.015, energy_return=0.60),
    "Hard, new":      dict(k0=95e3, x_max=0.015, energy_return=0.60),
    # ASSUMPTION (illustrative only): wear makes the foam 50% stiffer and
    # loses 15% of its usable thickness. Measure real worn shoes instead!
    "Soft, worn":     dict(k0=61e3 * 1.5, x_max=0.015 * 0.85, energy_return=0.55),
    # ASSUMPTION: a 'super-shoe' style foam - soft but more resilient
    "Resilient foam": dict(k0=61e3, x_max=0.015, energy_return=0.80),
}
# ASSUMPTION: human heel pad (fat pad under the heel bone)
HEEL_PAD = dict(k0=30e3, x_max=0.011)

# --- Test rig (ASTM F1976-style) -----------------------------------------
STRIKER_MASS = 8.5          # kg
IMPACT_ENERGY = 5.0         # J  (nominal for running shoes)

# --- Runner ---------------------------------------------------------------
EFFECTIVE_MASS_FRACTION = 0.08   # ASSUMPTION: foot + shank, fraction of body mass
TOUCHDOWN_SPEED = 1.0            # m/s  ASSUMPTION: heel vertical speed at contact
BODY_MASSES = [55.0, 70.0, 85.0]  # kg


# --------------------------------------------------------------------------
def compression_table(layers):
    """Force-compression table for foam layers in series.
    For one layer:  x(F) = F / (k0 + F / x_max)   (inverse of the foam law)."""
    force = np.concatenate([[0.0], np.geomspace(1e-2, 1e5, 8000)])
    comp = np.zeros_like(force)
    for layer in layers:
        comp += force / (layer["k0"] + force / layer["x_max"])
    return comp, force


def drop(mass, speed, layers, beta, dt=1e-5, t_max=0.1):
    """A mass hitting the foam layers at `speed`. Returns time, force, compression,
    and the rebound speed. 4th-order Runge-Kutta."""
    comp_tab, force_tab = compression_table(layers)

    def accel(x, v):  # x = compression, v = compression rate
        if x <= 0:
            return 0.0, 0.0
        f = max(np.interp(x, comp_tab, force_tab) * (1 + beta * v), 0.0)
        return -f / mass, f

    x, v = 0.0, speed
    t_out, f_out, x_out = [], [], []
    for i in range(int(t_max / dt)):
        # Runge-Kutta: four estimates of the slope, then a weighted average
        k1v, f = accel(x, v)
        k1x = v
        k2v, _ = accel(x + dt / 2 * k1x, v + dt / 2 * k1v)
        k2x = v + dt / 2 * k1v
        k3v, _ = accel(x + dt / 2 * k2x, v + dt / 2 * k2v)
        k3x = v + dt / 2 * k2v
        k4v, _ = accel(x + dt * k3x, v + dt * k3v)
        k4x = v + dt * k3v
        t_out.append(i * dt), f_out.append(f), x_out.append(x)
        x += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        if x <= 0 and i > 10:   # mass has left the foam
            break
    return np.array(t_out), np.array(f_out), np.array(x_out), -v


def beta_for_energy_return(shoe, target):
    """Damping beta giving the target energy return in the drop test."""
    speed = np.sqrt(2 * IMPACT_ENERGY / STRIKER_MASS)
    lo, hi = 0.0, 20.0
    for _ in range(40):  # bisection: more damping -> less energy returned
        mid = 0.5 * (lo + hi)
        *_, v_out = drop(STRIKER_MASS, speed, [shoe], mid, dt=2e-5)
        if (v_out / speed) ** 2 > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def loading_rate(t, f):
    """Average loading rate between 20% and 80% of the peak (as in Davis et al. 2016)."""
    peak = f.max()
    i20 = np.argmax(f >= 0.2 * peak)
    i80 = np.argmax(f >= 0.8 * peak)
    return (f[i80] - f[i20]) / (t[i80] - t[i20])


# --------------------------------------------------------------------------
def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    betas = {name: beta_for_energy_return(s, s["energy_return"]) for name, s in SHOES.items()}

    # ---------------- A) drop-test rig ------------------------------------
    speed = np.sqrt(2 * IMPACT_ENERGY / STRIKER_MASS)
    print(f"A) ASTM F1976-style drop test: {STRIKER_MASS} kg striker, {IMPACT_ENERGY} J "
          f"(drop height {1000 * speed**2 / (2 * G):.0f} mm, impact {speed:.2f} m/s)")
    print(f"   {'shoe':<16}{'peak g':>8}{'peak N':>8}{'max mm':>8}{'contact ms':>12}{'energy ret.':>13}")
    fig_a, (ax_a1, ax_a2) = plt.subplots(1, 2, figsize=(10, 3.8))
    drop_results = {}
    for name, shoe in SHOES.items():
        t, f, x, v_out = drop(STRIKER_MASS, speed, [shoe], betas[name])
        drop_results[name] = (t, f, x)
        print(f"   {name:<16}{f.max() / (STRIKER_MASS * G):8.1f}{f.max():8.0f}"
              f"{x.max() * 1e3:8.1f}{t[-1] * 1e3:12.1f}{(v_out / speed) ** 2:13.2f}")
        ax_a1.plot(t * 1e3, f / (STRIKER_MASS * G), lw=2, label=name)
        ax_a2.plot(x * 1e3, f, lw=2, label=name)
    ax_a1.set(xlabel="Time (ms)", ylabel="Striker deceleration (g)",
              title="Drop test: what the accelerometer sees")
    ax_a2.set(xlabel="Heel compression (mm)", ylabel="Force (N)",
              title="Force-compression loop (area = energy lost)")
    for ax in (ax_a1, ax_a2):
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig_a.tight_layout()
    fig_a.savefig(FIG_DIR / "shoe_drop_test_model.png", dpi=200)

    # ---------------- B) runner heel strike -------------------------------
    print(f"\nB) Heel-strike impact transient (effective mass "
          f"{EFFECTIVE_MASS_FRACTION:.0%} of body mass, {TOUCHDOWN_SPEED} m/s)")
    print(f"   {'body kg':>8}  {'shoe':<16}{'peak BW':>9}{'time ms':>9}{'LR BW/s':>9}")
    stiffness = np.linspace(40e3, 140e3, 21)
    fig_b, (ax_b1, ax_b2) = plt.subplots(1, 2, figsize=(10, 3.8))
    for m_body in BODY_MASSES:
        m_eff = EFFECTIVE_MASS_FRACTION * m_body
        weight = m_body * G
        lr = []
        for k in stiffness:
            shoe = dict(k0=k, x_max=0.015)
            t, f, _, _ = drop(m_eff, TOUCHDOWN_SPEED, [HEEL_PAD, shoe], betas["Soft, new"])
            lr.append(loading_rate(t, f / weight))
        ax_b2.plot(stiffness / 1e3, lr, lw=2, label=f"{m_body:.0f} kg runner")
        for name in ["Soft, new", "Hard, new", "Soft, worn"]:
            t, f, _, _ = drop(m_eff, TOUCHDOWN_SPEED, [HEEL_PAD, SHOES[name]], betas[name])
            print(f"   {m_body:8.0f}  {name:<16}{f.max() / weight:9.2f}"
                  f"{t[np.argmax(f)] * 1e3:9.1f}{loading_rate(t, f / weight):9.0f}")
            if m_body == 70.0:
                ax_b1.plot(t * 1e3, f / weight, lw=2, label=name)
    ax_b1.set(xlabel="Time from heel contact (ms)", ylabel="Impact force (BW)",
              title="Impact transient, 70 kg runner")
    ax_b2.axvspan(61, 95, color="grey", alpha=0.15, label="soft-hard range tested\nby Malisoux et al. 2020")
    ax_b2.set(xlabel="Shoe heel stiffness (N/mm)", ylabel="Loading rate (BW/s)",
              title="Loading rate vs shoe stiffness")
    for ax in (ax_b1, ax_b2):
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig_b.tight_layout()
    fig_b.savefig(FIG_DIR / "shoe_heel_strike_model.png", dpi=200)

    # Report figure: one panel from each study
    fig_r, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    for name, (t, f, x) in drop_results.items():
        ax1.plot(t * 1e3, f / (STRIKER_MASS * G), lw=2, label=name)
    ax1.set(xlabel="Time (ms)", ylabel="Striker deceleration (g)",
            title="(a) Predicted drop-test response (8.5 kg, 5 J)")
    for line in ax_b2.get_lines():
        ax2.plot(line.get_xdata(), line.get_ydata(), lw=2, label=line.get_label())
    ax2.axvspan(61, 95, color="grey", alpha=0.15, label="Malisoux et al. 2020 range")
    ax2.set(xlabel="Shoe heel stiffness (N/mm)", ylabel="Impact loading rate (BW/s)",
            title="(b) Runner impact loading rate vs shoe stiffness")
    for ax in (ax1, ax2):
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig_r.tight_layout()
    fig_r.savefig(FIG_DIR / "report_fig_shoe_model.png", dpi=200)
    print(f"\nFigures saved in: {FIG_DIR}")


if __name__ == "__main__":
    main()
