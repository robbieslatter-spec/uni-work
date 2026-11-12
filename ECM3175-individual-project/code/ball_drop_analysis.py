#!/usr/bin/env python3
"""
ball_drop_analysis.py  -  ECM3175 Individual Project, preliminary EXPERIMENT
===========================================================================

A quick experiment you can do this week (no lab needed, about 1 hour):
drop a football from 2.0 m onto a hard floor at different inflation
pressures, film it, and measure how high it bounces back.

From each drop this script calculates:
  * coefficient of restitution   COR = sqrt(rebound height / drop height)
    (energy lost by the ball, ignoring air resistance)
  * contact time with the floor, if you counted slow-motion frames
and compares the contact time with heading_impact_model.py.

Its main output is the COR to feed into the heading model:
    python heading_impact_model.py --cor <value printed by this script>

HOW TO DO THE EXPERIMENT
------------------------
 1. Stick a tape measure vertically to a wall (0 m at the floor).
 2. Pump the ball to the target pressure with a pump that has a gauge.
    Law 2 range is 0.6-1.1 atm (about 8.8-16.2 psi, 0.61-1.11 bar).
    Use e.g. 0.6, 0.85 and 1.1 atm (8.8, 12.5, 16.2 psi).
 3. Hold the ball so its BOTTOM is at 2.00 m and release it without spin.
 4. Film side-on (phone slow-motion, 240 fps if possible), level with
    the expected rebound height, about 2-3 m from the wall.
 5. Read the rebound height = height of the ball's BOTTOM at the top of the
    bounce. Repeat 5 times per pressure.
 6. (Optional) count the slow-motion frames in which the ball touches the
    floor. At 240 fps one frame = 4.2 ms, so this is only a rough check.
 7. Type the results into a CSV file laid out like data/ball_drop_TEMPLATE.csv

HOW TO RUN
----------
    python ball_drop_analysis.py data/my_ball_drops.csv
    python ball_drop_analysis.py            (runs the EXAMPLE file to show the
                                             output - those are NOT real data)
"""

import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import heading_impact_model as hm

HERE = Path(__file__).resolve().parent
EXAMPLE_FILE = HERE / "data" / "ball_drop_EXAMPLE_not_real.csv"
FIG_DIR = HERE.parent / "figures"


def read_csv(path):
    """Read the drop data. Lines starting with # are comments."""
    rows = []
    with open(path) as fh:
        lines = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    header = [h.strip() for h in lines[0].split(",")]
    for ln in lines[1:]:
        values = [v.strip() for v in ln.split(",")]
        row = dict(zip(header, values))
        rows.append({
            "pressure_atm": float(row["pressure_atm"]),
            "drop_height_m": float(row["drop_height_m"]),
            "rebound_height_m": float(row["rebound_height_m"]),
            "contact_frames": float(row["contact_frames"]) if row.get("contact_frames") else np.nan,
            "fps": float(row["fps"]) if row.get("fps") else np.nan,
        })
    return rows


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EXAMPLE_FILE
    is_example = "EXAMPLE" in path.name.upper()
    if is_example:
        print("!" * 70)
        print("  Using the EXAMPLE file: these numbers are made up to show how the")
        print("  script works. Do NOT put them in your report - use your own data.")
        print("!" * 70)

    rows = read_csv(path)
    pressures = sorted({r["pressure_atm"] for r in rows})

    print(f"\n{'pressure':>9} {'drops':>6} {'COR mean':>9} {'COR SD':>7} "
          f"{'contact ms':>11} {'model ms':>9}")
    summary = []
    for p in pressures:
        drops = [r for r in rows if r["pressure_atm"] == p]
        cor = np.array([np.sqrt(r["rebound_height_m"] / r["drop_height_m"]) for r in drops])
        tc = np.array([r["contact_frames"] / r["fps"] for r in drops]) * 1e3  # ms
        h_drop = np.mean([r["drop_height_m"] for r in drops])
        # model prediction of the contact time with a rigid flat floor
        alpha = hm.alpha_for_cor(cor.mean(), p_gauge_atm=p, drop_height=h_drop)
        v = np.sqrt(2 * hm.G * h_drop)
        sim = hm.simulate(v, p, alpha, r_head=np.inf, rigid_wall=True, dt=2e-5)
        tc_model = hm.contact_time(sim["t"], sim["force"])[0] * 1e3
        tc_mean = np.nanmean(tc) if np.any(~np.isnan(tc)) else np.nan
        summary.append((p, cor, tc, tc_model))
        print(f"{p:9.2f} {len(drops):6d} {cor.mean():9.3f} {cor.std(ddof=1):7.3f} "
              f"{tc_mean:11.1f} {tc_model:9.1f}")

    # COR to use in the heading model: the pressure closest to 0.85 atm
    p_ref, cor_ref, *_ = min(summary, key=lambda s: abs(s[0] - 0.85))
    print(f"\nUse this in the heading model (ball at {p_ref:.2f} atm):")
    print(f"    python heading_impact_model.py --cor {cor_ref.mean():.3f}")

    # ---- figure -----------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))
    for p, cor, tc, tc_model in summary:
        ax1.plot([p] * len(cor), cor, "o", color="tab:blue", alpha=0.4)
        ax1.errorbar(p, cor.mean(), yerr=cor.std(ddof=1), fmt="s", color="black",
                     capsize=4)
        if np.any(~np.isnan(tc)):
            ax2.plot([p] * len(tc), tc, "o", color="tab:blue", alpha=0.4)
        ax2.plot(p, tc_model, "D", color="tab:red")
    ax1.set(xlabel="Ball gauge pressure (atm)", ylabel="Coefficient of restitution",
            title="Ball COR from 2 m drop (mean +/- SD)")
    ax2.set(xlabel="Ball gauge pressure (atm)", ylabel="Contact time (ms)",
            title="Contact time: video (blue) vs model (red)")
    for ax in (ax1, ax2):
        ax.grid(alpha=0.3)
        if is_example:
            ax.text(0.5, 0.5, "EXAMPLE DATA\nNOT REAL", transform=ax.transAxes,
                    fontsize=26, color="red", alpha=0.25, ha="center", va="center",
                    rotation=20, fontweight="bold")
    fig.tight_layout()
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    name = "ball_drop_EXAMPLE_not_real.png" if is_example else "ball_drop_results.png"
    fig.savefig(FIG_DIR / name, dpi=200)
    print(f"\nFigure saved: {FIG_DIR / name}")


if __name__ == "__main__":
    main()
