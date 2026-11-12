#!/usr/bin/env python3
"""
gantt_chart.py  -  draws the project Gantt chart for the preliminary report.

Edit the TASKS list below (name, start date, end date, phase) and re-run:
    python gantt_chart.py           ->  ../figures/gantt_chart.png
A task whose start and end dates are the same is drawn as a milestone (diamond).
Dates for 2027 term/vacation shading are approximate - check the University
of Exeter term dates page and change VACATIONS if needed.
"""

from datetime import date, timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"

# (task name, start, end, phase)
TASKS = [
    ("Weekly supervisor meetings + logbook", date(2026, 12, 7), date(2027, 4, 30), "Management"),
    ("Order parts (GBP 75 budget, order form)", date(2026, 12, 7), date(2026, 12, 11), "Design"),
    ("Rig concept design + CAD", date(2026, 12, 7), date(2026, 12, 18), "Design"),
    ("Write RAMS (risk assessment + method statement)", date(2026, 12, 7), date(2026, 12, 16), "Design"),
    ("RAMS approval: supervisor, then module convenor", date(2026, 12, 16), date(2027, 1, 15), "Design"),
    ("RAMS approved: lab work can start", date(2027, 1, 15), date(2027, 1, 15), "Milestone"),
    ("Literature review chapter (expanded)", date(2026, 12, 14), date(2027, 1, 22), "Write"),
    ("Logging code + sensor bench test", date(2027, 1, 11), date(2027, 1, 29), "Build"),
    ("Build headform, necks and ball delivery", date(2027, 1, 15), date(2027, 2, 5), "Build"),
    ("Calibrate and validate rig vs model", date(2027, 2, 1), date(2027, 2, 19), "Build"),
    ("Methodology & theory chapter", date(2027, 2, 1), date(2027, 2, 19), "Write"),
    ("Rig validated (go / no-go)", date(2027, 2, 19), date(2027, 2, 19), "Milestone"),
    ("Main tests: speed x pressure x neck", date(2027, 2, 22), date(2027, 3, 12), "Test"),
    ("Extension: wet / vintage ball (if budget)", date(2027, 3, 8), date(2027, 3, 19), "Test"),
    ("All data collected", date(2027, 3, 19), date(2027, 3, 19), "Milestone"),
    ("Experimental work chapter", date(2027, 3, 1), date(2027, 3, 19), "Write"),
    ("Data analysis + model refinement", date(2027, 3, 1), date(2027, 4, 2), "Analyse"),
    ("Decommission rig, return equipment", date(2027, 3, 29), date(2027, 4, 2), "Test"),
    ("Results, discussion, abstract", date(2027, 3, 22), date(2027, 4, 9), "Write"),
    ("Full draft to supervisor", date(2027, 4, 9), date(2027, 4, 9), "Milestone"),
    ("Revise, proofread, check 35 pages", date(2027, 4, 12), date(2027, 4, 30), "Write"),
    ("Final report deadline (12 noon)", date(2027, 5, 3), date(2027, 5, 3), "Milestone"),
    ("Interview preparation", date(2027, 5, 4), date(2027, 5, 18), "Write"),
    ("Interview (19-28 May)", date(2027, 5, 19), date(2027, 5, 28), "Write"),
]

# Shaded periods (approximate - check the official term dates)
VACATIONS = [
    ("Christmas vacation", date(2026, 12, 19), date(2027, 1, 10)),
    ("Easter vacation (check dates)", date(2027, 3, 27), date(2027, 4, 25)),
]

COLOURS = {
    "Management": "#9e9e9e", "Design": "#4e79a7", "Build": "#f28e2b",
    "Test": "#e15759", "Analyse": "#76b7b2", "Write": "#59a14f", "Milestone": "black",
}


def main():
    fig, ax = plt.subplots(figsize=(11, 7.0))
    for name, start, end in VACATIONS:
        ax.axvspan(start, end + timedelta(days=1), color="grey", alpha=0.12)
        ax.text(start + (end - start) / 2, -0.9, name, ha="center", va="center",
                fontsize=8, color="dimgrey")

    for row, (name, start, end, phase) in enumerate(TASKS):
        if start == end:  # milestone
            ax.plot(start, row, marker="D", ms=9, color=COLOURS["Milestone"])
            ax.text(start + timedelta(days=3), row, start.strftime("%d %b"),
                    va="center", fontsize=8)
        else:
            ax.barh(row, (end - start).days + 1, left=start, height=0.6,
                    color=COLOURS[phase], edgecolor="black", linewidth=0.4)

    ax.set_yticks(range(len(TASKS)))
    ax.set_yticklabels([t[0] for t in TASKS], fontsize=9)
    ax.set_ylim(len(TASKS) - 0.4, -1.5)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax.grid(axis="x", which="major", alpha=0.5)
    ax.grid(axis="x", which="minor", alpha=0.15)
    ax.set_xlim(date(2026, 12, 1), date(2027, 6, 1))

    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for p, c in COLOURS.items() if p != "Milestone"]
    handles.append(plt.Line2D([], [], marker="D", color="black", ls="", ms=8))
    labels = [p for p in COLOURS if p != "Milestone"] + ["Milestone"]
    ax.legend(handles, labels, loc="lower left", fontsize=8, ncol=4, framealpha=0.9)
    fig.tight_layout()
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "gantt_chart.png", dpi=200)
    print(f"Saved {FIG_DIR / 'gantt_chart.png'}")


if __name__ == "__main__":
    main()
