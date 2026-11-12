#!/usr/bin/env python3
"""
heading_impact_model.py  -  ECM3175 Individual Project, preliminary work
=======================================================================

WHAT THIS DOES
--------------
Simulates a football hitting a head and predicts, for different ball speeds,
inflation pressures and neck "stiffness":
  * peak linear head acceleration (g)   <- what a head-mounted sensor measures
  * ball-head contact time (ms)
  * peak contact force (N)
  * HIC15 (Head Injury Criterion), a standard engineering severity index

THE MODEL (1-D: three masses in a line)
---------------------------------------
      ball  ==contact==>  HEAD  --[neck spring k_n + damper c_n]--  TORSO
      m_b                 m_h                                        m_t

Ball-head contact force (thin pressurised ball, membrane model):

    F = p(d) * pi * a(d)^2 * (1 + alpha * d_dot)          (and F >= 0)

    d       how far the ball is squashed against the head          [m]
    a       radius of the flattened contact patch, from the
            geometry of two overlapping spheres (ball radius R_b,
            forehead radius R_h). Flat floor: R_h = infinity        [m]
    p       gauge pressure inside the ball. Squashing the ball makes
            its volume smaller, so p rises (adiabatic air, gamma=1.4) [Pa]
    alpha   Hunt-Crossley damping [s/m]. It is chosen so that the
            ball's coefficient of restitution (COR) when dropped onto
            a rigid floor matches a target value (your measurement!)

Neck force on the head:   F_n = k_n*(x_h - x_t) + c_n*(v_h - v_t)

HOW TO RUN
----------
    python heading_impact_model.py               (default COR = 0.82)
    python heading_impact_model.py --cor 0.79    (use the COR you measured
                                                  with ball_drop_analysis.py)
    python heading_impact_model.py --show        (also open the plots)

Figures go to ../figures/ and a results table to ../figures/heading_summary.csv

IMPORTANT
---------
This is a simplified model. Its job in the project is to:
  1. predict the size and duration of head accelerations, so you can choose
     a sensor (range, sampling rate) and design the test rig, and
  2. give hypotheses (pressure, speed, neck coupling) to test with the rig.
Every value marked ASSUMPTION should be checked, measured or justified.
"""

import argparse
import csv
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # save figures without needing a screen
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# PARAMETERS
# --------------------------------------------------------------------------
G = 9.81                    # m/s^2
ATM = 101_325.0             # Pa, 1 standard atmosphere
GAMMA = 1.4                 # air, fast compression -> adiabatic

BALL_MASS = 0.43            # kg   Law 2 (Laws of the Game): 0.41-0.45 kg
BALL_CIRCUMFERENCE = 0.69   # m    Law 2: 0.68-0.70 m
BALL_RADIUS = BALL_CIRCUMFERENCE / (2 * np.pi)

HEAD_MASS = 4.5             # kg   ASSUMPTION: adult head (Hybrid III 50th
                            #      percentile male head assembly = 4.54 kg)
FOREHEAD_RADIUS = 0.09      # m    ASSUMPTION: curvature of the forehead
TORSO_MASS = 30.0           # kg   ASSUMPTION: upper-body mass the neck can
                            #      couple to the head during the impact

# Neck used for the speed/pressure study: a weakly coupled ("relaxed") neck.
NECK_K = 2_000.0            # N/m    ASSUMPTION
NECK_C = 20.0               # N s/m  ASSUMPTION

DEFAULT_COR = 0.82          # ASSUMPTION until you measure your own ball.
                            # FIFA rebound test: 2 m drop onto steel,
                            # rebound ~1.2-1.65 m  ->  COR ~0.77-0.91
COR_DROP_HEIGHT = 2.0       # m, the drop test used to define the COR

PRESSURES_ATM = [0.6, 0.85, 1.1]   # gauge pressure, Law 2 range 0.6-1.1 atm
LOW_PRESSURE_ATM = 0.3             # below Law 2 minimum ("what if" case)

# Published measurement used as a sanity check (human subjects heading a
# ball): Naunheim et al. (2003), Med Sci Sports Exerc 35(8):1406-1412.
NAUNHEIM_SPEED = np.array([9.0, 12.0])          # m/s
NAUNHEIM_ACCEL_G = np.array([158.0, 199.0]) / G  # m/s^2 -> g

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"


# --------------------------------------------------------------------------
# PHYSICS
# --------------------------------------------------------------------------
def contact_geometry(d, r_ball, r_head):
    """Contact patch radius squared (a^2) and volume pushed out of the ball (dV)
    when the ball is squashed by d against a rigid sphere of radius r_head
    (r_head = inf means a flat floor/plate). Exact sphere-sphere geometry."""
    d = np.maximum(d, 0.0)
    flat = np.isinf(r_head)

    # Ball against a flat surface (spherical cap)
    a2_flat = 2 * r_ball * d - d**2
    dv_flat = np.pi * d**2 * (3 * r_ball - d) / 3

    # Ball against a curved forehead (lens-shaped overlap of two spheres)
    r1 = r_ball
    r2 = np.where(flat, 1.0, r_head)  # dummy value where flat (not used)
    D = r1 + r2 - d                   # distance between the two centres
    x = (D**2 - r2**2 + r1**2) / (2 * D)
    a2_sph = r1**2 - x**2
    dv_sph = (np.pi * (r1 + r2 - D) ** 2
              * (D**2 + 2 * D * r1 - 3 * r1**2 + 2 * D * r2 + 6 * r1 * r2 - 3 * r2**2)
              / (12 * D))

    a2 = np.where(flat, a2_flat, a2_sph)
    dv = np.where(flat, dv_flat, dv_sph)
    return np.maximum(a2, 0.0), np.maximum(dv, 0.0)


def contact_force(d, d_dot, p0_gauge, alpha, r_ball, r_head):
    """Ball contact force [N] (pressure x contact area, Hunt-Crossley damping)."""
    a2, dv = contact_geometry(d, r_ball, r_head)
    v0 = 4.0 / 3.0 * np.pi * r_ball**3
    p_abs = (p0_gauge + ATM) * (v0 / (v0 - dv)) ** GAMMA
    f_elastic = (p_abs - ATM) * np.pi * a2
    f = f_elastic * (1.0 + alpha * d_dot)
    return np.where(d > 0, np.maximum(f, 0.0), 0.0)


def simulate(v_impact, p_gauge_atm, alpha, k_neck=NECK_K, c_neck=NECK_C,
             m_ball=BALL_MASS, m_head=HEAD_MASS, m_torso=TORSO_MASS,
             r_ball=BALL_RADIUS, r_head=FOREHEAD_RADIUS,
             rigid_wall=False, t_end=0.030, dt=1e-5):
    """Simulate many impacts at once. Any input can be a number or a numpy
    array (arrays must have the same shape). Uses 4th-order Runge-Kutta.

    Returns a dict with time t [s] and, for every case, the contact force F [N],
    head acceleration a_head [m/s^2], and final ball/head velocities."""
    (v_impact, p_gauge_atm, alpha, k_neck, c_neck, m_ball, m_head, m_torso,
     r_ball, r_head) = [np.ravel(a).astype(float) for a in np.broadcast_arrays(
        v_impact, p_gauge_atm, alpha, k_neck, c_neck, m_ball, m_head, m_torso,
        r_ball, r_head)]
    p0 = p_gauge_atm * ATM
    n_cases = v_impact.size
    n_steps = int(round(t_end / dt))

    # state: ball x/v, head x/v, torso x/v.  x = 0 at first contact.
    s = np.zeros((6, n_cases))
    s[1] = v_impact  # ball moving towards the head (+x)

    def derivs(state):
        xb, vb, xh, vh, xt, vt = state
        f = contact_force(xb - xh, vb - vh, p0, alpha, r_ball, r_head)
        f_neck = k_neck * (xh - xt) + c_neck * (vh - vt)
        ab = -f / m_ball
        if rigid_wall:
            ah = np.zeros_like(f)
            at = np.zeros_like(f)
        else:
            ah = (f - f_neck) / m_head
            at = f_neck / m_torso
        return np.array([vb, ab, vh, ah, vt, at]), f, ah

    t = np.arange(n_steps + 1) * dt
    force = np.zeros((n_cases, n_steps + 1))
    a_head = np.zeros((n_cases, n_steps + 1))
    for i in range(n_steps):
        k1, f, ah = derivs(s)
        force[:, i], a_head[:, i] = f, ah
        k2, _, _ = derivs(s + 0.5 * dt * k1)
        k3, _, _ = derivs(s + 0.5 * dt * k2)
        k4, _, _ = derivs(s + dt * k3)
        s = s + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    _, f, ah = derivs(s)
    force[:, -1], a_head[:, -1] = f, ah

    return {"t": t, "force": force, "a_head": a_head,
            "v_ball_end": s[1], "v_head_end": s[3], "v_impact": v_impact}


def contact_time(t, force):
    """Duration [s] of the first continuous period with force > 0, per case."""
    in_contact = force > 0
    out = np.zeros(force.shape[0])
    for i, row in enumerate(in_contact):
        idx = np.flatnonzero(row)
        if idx.size == 0:
            continue
        gaps = np.flatnonzero(np.diff(idx) > 1)
        last = idx[gaps[0]] if gaps.size else idx[-1]
        out[i] = t[last] - t[idx[0]]
    return out


def hic15(t, accel_g):
    """Head Injury Criterion (HIC15) for one acceleration trace in g.
    HIC = max over windows (t2 - t1 <= 15 ms) of
          (t2 - t1) * [average acceleration over the window] ** 2.5"""
    a = np.abs(accel_g)
    dt = t[1] - t[0]
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (a[1:] + a[:-1]) * dt)])
    best = 0.0
    for w in range(1, min(int(round(0.015 / dt)), len(t) - 1) + 1):
        dur = w * dt
        avg = (cum[w:] - cum[:-w]) / dur
        best = max(best, float(np.max(dur * avg**2.5)))
    return best


def alpha_for_cor(target_cor, p_gauge_atm=0.85, drop_height=COR_DROP_HEIGHT):
    """Find the damping alpha that makes the ball bounce off a rigid flat floor
    with the target COR (ball dropped from drop_height)."""
    v = np.sqrt(2 * G * drop_height)

    def cor_for(alphas):
        r = simulate(v, p_gauge_atm, alphas, r_head=np.inf, rigid_wall=True,
                     t_end=0.03, dt=2e-5)
        return -r["v_ball_end"] / v

    alphas = np.linspace(0.0, 0.5, 201)
    cors = cor_for(alphas)                      # decreases as alpha increases
    if not (cors.min() <= target_cor <= cors.max()):
        raise ValueError(f"COR {target_cor} outside model range "
                         f"{cors.min():.2f}-{cors.max():.2f}")
    a0 = np.interp(target_cor, cors[::-1], alphas[::-1])
    fine = np.linspace(max(a0 - 0.005, 0.0), a0 + 0.005, 101)  # refine
    return float(np.interp(target_cor, cor_for(fine)[::-1], fine[::-1]))


# --------------------------------------------------------------------------
# STUDIES + FIGURES
# --------------------------------------------------------------------------
def study_speed_pressure(alpha):
    speeds = np.linspace(4, 25, 43)
    pressures = PRESSURES_ATM + [LOW_PRESSURE_ATM]
    S, P = np.meshgrid(speeds, pressures)
    r = simulate(S, P, alpha)
    peak_g = r["a_head"].max(axis=1).reshape(S.shape) / G
    return speeds, pressures, peak_g


NECK_DAMPING_RATIO = 0.3    # ASSUMPTION: neck damping as a fraction of critical


def study_neck(alpha, speed=12.0, p_atm=0.85):
    ks = np.logspace(3, 7, 61)
    c = 2 * NECK_DAMPING_RATIO * np.sqrt(ks * HEAD_MASS)
    r = simulate(speed, p_atm, alpha, k_neck=ks, c_neck=c)
    peak_g = r["a_head"].max(axis=1) / G
    # limits: head on its own, and head + torso moving as one body
    free = simulate(speed, p_atm, alpha, k_neck=0.0, c_neck=0.0)
    joined = simulate(speed, p_atm, alpha, k_neck=0.0, c_neck=0.0,
                      m_head=HEAD_MASS + TORSO_MASS)
    tc = contact_time(free["t"], free["force"])[0]
    return ks, peak_g, free["a_head"].max() / G, joined["a_head"].max() / G, tc


def plot_speed_pressure(ax, speeds, pressures, peak_g):
    styles = {0.6: "-", 0.85: "-", 1.1: "-", LOW_PRESSURE_ATM: "--"}
    for p, row in zip(pressures, peak_g):
        label = f"{p:.2f} atm" + ("  (below Law 2 minimum)" if p < 0.6 else "")
        ax.plot(speeds, row, styles.get(p, "-"), lw=2, label=label)
    ax.plot(NAUNHEIM_SPEED, NAUNHEIM_ACCEL_G, "ks", ms=7,
            label="Measured, Naunheim et al. 2003")
    ax.set_xlabel("Ball speed at impact (m/s)")
    ax.set_ylabel("Peak head acceleration (g)")
    ax.set_title("(a) Effect of ball speed and inflation pressure")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, title="Ball gauge pressure", title_fontsize=8)


def plot_neck(ax, ks, peak_g, free_g, joined_g, speed=12.0):
    ax.semilogx(ks, peak_g, lw=2, color="tab:purple", label="model")
    ax.axhline(free_g, ls="--", color="grey")
    ax.axhline(joined_g, ls=":", color="grey")
    ax.axhline(NAUNHEIM_ACCEL_G[1], ls="-", lw=6, color="black", alpha=0.15,
               label="measured at 12 m/s (Naunheim et al. 2003)")
    ax.text(ks[0], free_g, f"  head on its own ({HEAD_MASS:.1f} kg)",
            va="bottom", fontsize=8)
    ax.text(ks[0], joined_g,
            f"  head + torso as one body ({HEAD_MASS + TORSO_MASS:.1f} kg)",
            va="bottom", fontsize=8)
    ax.legend(fontsize=8, loc="center left")
    ax.set_xlabel("Neck coupling stiffness k_n (N/m)")
    ax.set_ylabel("Peak head acceleration (g)")
    ax.set_title(f"(b) Effect of neck coupling ({speed:.0f} m/s, 0.85 atm)")
    ax.grid(alpha=0.3, which="both")


def plot_time_history(alpha, speed=12.0):
    r = simulate(speed, np.array(PRESSURES_ATM), alpha, t_end=0.025)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))
    for i, p in enumerate(PRESSURES_ATM):
        ax1.plot(r["t"] * 1e3, r["force"][i], lw=2, label=f"{p:.2f} atm")
        ax2.plot(r["t"] * 1e3, r["a_head"][i] / G, lw=2, label=f"{p:.2f} atm")
    ax1.set(xlabel="Time (ms)", ylabel="Ball-head contact force (N)",
            title=f"Contact force, ball at {speed:.0f} m/s")
    ax2.set(xlabel="Time (ms)", ylabel="Head acceleration (g)",
            title="Head acceleration (what the sensor sees)")
    for ax in (ax1, ax2):
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)
    fig.tight_layout()
    return fig


def summary_table(alpha):
    rows = []
    speeds = [9.0, 12.0, 15.0, 20.0]
    for p in PRESSURES_ATM + [LOW_PRESSURE_ATM]:
        r = simulate(np.array(speeds), p, alpha)
        tc = contact_time(r["t"], r["force"])
        for i, v in enumerate(speeds):
            a_g = r["a_head"][i] / G
            rows.append({
                "ball_speed_m_s": v,
                "pressure_atm": p,
                "peak_head_accel_g": round(float(a_g.max()), 1),
                "contact_time_ms": round(float(tc[i] * 1e3), 2),
                "peak_force_N": round(float(r["force"][i].max()), 0),
                "HIC15": round(hic15(r["t"], a_g), 2),
                "COR_ball_head": round(float(-(r["v_ball_end"][i] - r["v_head_end"][i]) / v), 3),
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cor", type=float, default=DEFAULT_COR,
                        help="ball COR from a 2 m drop onto a rigid floor (default 0.82)")
    parser.add_argument("--show", action="store_true", help="open the figures on screen")
    args = parser.parse_args()
    if args.show:
        plt.switch_backend("TkAgg")
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Calibrating ball damping so that COR = {args.cor:.3f} for a "
          f"{COR_DROP_HEIGHT:.1f} m drop ...")
    alpha = alpha_for_cor(args.cor)
    print(f"  Hunt-Crossley damping alpha = {alpha:.4f} s/m\n")

    speeds, pressures, peak_g = study_speed_pressure(alpha)
    ks, neck_g, free_g, joined_g, tc_free = study_neck(alpha)

    # Figure for the report: two panels side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    plot_speed_pressure(ax1, speeds, pressures, peak_g)
    plot_neck(ax2, ks, neck_g, free_g, joined_g)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "report_fig_heading_model.png", dpi=200)

    # Same panels as separate figures, plus time histories
    for name, plotter, data in [
        ("heading_accel_vs_speed.png", plot_speed_pressure, (speeds, pressures, peak_g)),
        ("heading_neck_stiffness.png", plot_neck, (ks, neck_g, free_g, joined_g)),
    ]:
        f, ax = plt.subplots(figsize=(6.5, 4.5))
        plotter(ax, *data)
        f.tight_layout()
        f.savefig(FIG_DIR / name, dpi=200)
    plot_time_history(alpha).savefig(FIG_DIR / "heading_time_history.png", dpi=200)

    rows = summary_table(alpha)
    with open(FIG_DIR / "heading_summary.csv", "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"{'speed':>6} {'pressure':>9} {'peak g':>7} {'contact':>8} "
          f"{'force':>7} {'HIC15':>6} {'COR':>6}")
    print(f"{'(m/s)':>6} {'(atm)':>9} {'':>7} {'(ms)':>8} {'(N)':>7} {'':>6} {'':>6}")
    for r in rows:
        print(f"{r['ball_speed_m_s']:6.0f} {r['pressure_atm']:9.2f} "
              f"{r['peak_head_accel_g']:7.1f} {r['contact_time_ms']:8.2f} "
              f"{r['peak_force_N']:7.0f} {r['HIC15']:6.2f} {r['COR_ball_head']:6.3f}")

    # Numbers that feed straight into the rig/sensor design
    worst_g = max(r["peak_head_accel_g"] for r in rows)
    shortest = min(r["contact_time_ms"] for r in rows if r["contact_time_ms"] > 0)
    # neck stiffness at which the model matches the measured value at 12 m/s
    k_match = np.interp(NAUNHEIM_ACCEL_G[1], neck_g[::-1], ks[::-1])
    k_20 = np.interp(0.8 * free_g, neck_g[::-1], ks[::-1])
    print("\nDesign checks for the test rig:")
    print(f"  Largest predicted head acceleration: {worst_g:.0f} g "
          f"-> sensor range must exceed this (e.g. +/-200 g)")
    print(f"  Shortest contact time: {shortest:.1f} ms -> at 3200 samples/s you get "
          f"~{shortest * 3.2:.0f} points per impact (aim for 20+)")
    print(f"  Free-head contact time at 12 m/s: {tc_free * 1e3:.1f} ms")
    print(f"  Neck coupling needed to cut head acceleration by 20%: "
          f"k_n ~ {k_20 / 1e3:.0f} kN/m")
    print(f"  Neck coupling at which the model matches the measured 12 m/s value "
          f"({NAUNHEIM_ACCEL_G[1]:.1f} g): k_n ~ {k_match / 1e3:.0f} kN/m")
    print(f"\nFigures and table saved in: {FIG_DIR}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
