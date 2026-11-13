# ECM3175 Individual Project: Sport Injury Biomechanics

Start here. Every guide is also a **Word document** (`.docx`) with the same number: `0_START_HERE.docx`, `1_project_ideas.docx` and so on, with the references in `6_references.docx`. Use the Word versions to read, print or edit. The `.md` copies are for viewing on GitHub.

Read the files in this order:

| File | What it is |
|---|---|
| [`1_project_ideas.md`](1_project_ideas.md) | Your two ideas (heading, running shoes) expanded and improved, three new ideas, a comparison table and my recommendation |
| [`2_next_steps.md`](2_next_steps.md) | A dated to-do list up to the **4 Dec 2026** deadline, a draft email to your supervisor, meeting questions, kit list, risks, H&S |
| [`3_preliminary_report_OUTLINE.docx`](3_preliminary_report_OUTLINE.docx) | The preliminary report in the module's layout, with bullet points to turn into your own paragraphs. Figure 1, the Gantt chart and the risk table are already in it |
| [`4_full_project_plan.md`](4_full_project_plan.md) | **The whole-project plan to May 2027:** rules (£75 budget, RAMS, 35-page limit), where the marks are, final report blueprint, week-by-week tasks, decision gates, test matrix, interview prep |
| [`5_RAMS_starter.md`](5_RAMS_starter.md) | Starter content for your RAMS (risk assessment + method statement), which must be approved before any lab work |
| [`references.md`](references.md) | 40 references (including 2019–2025 studies), checked to exist, with a note on what each is useful for |
| `7_preliminary_report_TEMPLATE.docx` | **Write your preliminary report here.** Module layout with a slot for every paragraph (points to make, papers to cite, word target). Figure 1, the Gantt chart and the risk table are already in it. Tested to fit in 5 pages |
| [`8_preliminary_report_CHECKLIST.md`](8_preliminary_report_CHECKLIST.md) | Every task needed to finish and submit the preliminary report, in order, with dates |
| [`9_preliminary_report_GUIDE.md`](9_preliminary_report_GUIDE.md) | **Step-by-step guide to writing the preliminary report yourself:** each stage explained (understanding the task, aim and objectives, literature search and critical review, preliminary work, writing each section, figures, references, editing, submitting), with examples, common mistakes and "done when" checks |
| `10_introduction_DRAFT.docx` | Draft Introduction section (overview: why, what, how; aim; five objectives). Citations use the same numbering as the literature review |
| `11_literature_review_DRAFT.docx` | Draft Background and literature review section (five themed sub-sections ending in the research gap and questions), plus the combined, numbered reference list [1]–[22] for the Introduction and literature review |
| [`12_literature_notes.md`](12_literature_notes.md) | Research notes behind the review: search log, a literature matrix of all 22 sources (what they did, findings, limitations, use), a map of where the evidence agrees and conflicts, checks still needed, further reading |
| `code/` | Python models and analysis scripts (your preliminary work) |
| `figures/` | Figures and tables made by the code |

## The code

| Script | What it does | Makes |
|---|---|---|
| `heading_impact_model.py` | Simulates a football hitting a head: peak head acceleration, contact time, HIC15 for different ball speeds, pressures and neck stiffness | `report_fig_heading_model.png`, `heading_*.png`, `heading_summary.csv` |
| `ball_drop_analysis.py` | Analyses **your** ball-drop experiment (COR vs pressure) and tells you what to feed back into the heading model | `ball_drop_results.png` |
| `running_shoe_model.py` | Backup project: shoe drop-test rig and runner heel-strike impact for soft, hard and worn foams | `report_fig_shoe_model.png`, `shoe_*.png` |
| `gantt_chart.py` | Draws the Gantt chart; edit the task list at the top to change it | `gantt_chart.png` |

### How to run it (first time)
1. Install Python 3 if you don't have it. Anaconda, which is on the University PCs, already includes everything needed.
2. Open a terminal in this folder and install the two libraries:
   ```bash
   pip install -r code/requirements.txt
   ```
3. Go into the code folder:
   ```bash
   cd code
   ```
4. Run a script:
   ```bash
   python heading_impact_model.py
   ```
   The figures appear in `figures/`. Every script explains itself in the comment block at the top. Open it in VS Code or Spyder and read that first.

After your ball-drop experiment, type your numbers into a copy of `code/data/ball_drop_TEMPLATE.csv` (for example `my_ball_drops.csv`), then run:
```bash
python ball_drop_analysis.py data/my_ball_drops.csv
```
It prints a `--cor` value to use with the heading model.

## Important
- **AI rules:** Exeter puts each assessment in one of four GenAI categories: integrated, assisted, minimal or prohibited. Check which one applies to ECM3175 on ELE, or ask your supervisor, before using any of this text, and acknowledge AI help if required. Either way, write the report in your own words. You will have to explain everything in the interview.
- **`ball_drop_EXAMPLE_not_real.csv` is made-up example data.** It only shows how the script works. Never put those numbers in a report.
- **The models are simplified on purpose.** Values marked `ASSUMPTION` in the code must be justified or replaced with your own measurements. Saying this in your report, and explaining why, is good engineering practice.
