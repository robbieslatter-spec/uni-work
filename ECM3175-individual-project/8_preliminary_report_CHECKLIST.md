# Preliminary report checklist (deadline Fri 4 December 2026, 12:00)

Tick these off in order. You write the report in `7_preliminary_report_TEMPLATE.docx`, which has a slot for every paragraph.

| Finish by | Stage |
|---|---|
| Fri 20 Nov | 1. Set up |
| Fri 27 Nov | 2. Reading (start now, read alongside everything else) |
| Wed 25 Nov | 3. Preliminary work (model, ball-drop experiment, rig sketch) |
| Mon 30 Nov | 4. First draft written |
| Wed 2 Dec | 5–7. Figures, references, final checks |
| **Thu 3 Dec** | **8. Submit, one day early** |

---

## Stage 1: Set up (by Fri 20 Nov)
- [ ] **Email your supervisor and book a meeting.** The draft email is in `2_next_steps.md`.
- [ ] **At the meeting:**
  - agree the title and scope
  - ask what equipment exists (headform, ball launcher, accelerometers)
  - ask which GenAI category applies to ECM3175
  - ask whether they will read a draft, and by when
- [ ] **Start your logbook** and date every entry.
- [ ] **Set up your report file.** Open `7_preliminary_report_TEMPLATE.docx` and save a copy as `Prelim_Report_YourName.docx`. Fill in the cover page (title, name, programme, student number, candidate number, supervisor) and your name in the page header.
- [ ] Save it in **OneDrive** so it is backed up.

## Stage 2: Reading (by Fri 27 Nov)
- [ ] **Read in full:** [1] Mackay 2019, [4] Naunheim 2003 and [5] Shewchenko 2005.
- [ ] **Skim:** [2] Russell 2021, [3] Di Virgilio 2016, [6] Dezman 2013, [7] Caccese 2018, [8] Peek 2020 and [9] Rowson & Duma 2013.
- [ ] **For each paper, write four things in your logbook:**
  - what they did
  - what they found (with numbers)
  - one limitation
  - how it affects your project
- [ ] **Find 2–3 recent papers (2023–2026)** with the University library search. Try "soccer heading head acceleration", "football heading neck strength" and "instrumented mouthguard football". Add them to the background section.
- [ ] **Open the web sources** [10] and [11] (FA heading rules) and [12] (Law 2). Note the date you looked at each, for "last accessed".
- [ ] **Get full texts through the library** (ELE reading list or library search), not random websites.

## Stage 3: Preliminary work (by Wed 25 Nov)
**Model**
- [ ] Install Python and the libraries (see `README.md`), then run this in the `code` folder:
  ```bash
  python heading_impact_model.py
  ```
- [ ] Make sure you can explain Figure 1 in two sentences: what the axes show and what the lines mean.

**Ball-drop experiment (about 1 hour)**
- [ ] **Get the kit:** a size 5 football and a pump with a pressure gauge. Borrow them or use your own; department money can't refund personal purchases.
- [ ] **Set up:**
  - tape a tape measure vertically to a wall (0 m at the floor)
  - put your phone in slow-motion mode on a stack of books, 2–3 m away
- [ ] **Run the drops** at three pressures: 0.6, 0.85 and 1.1 atm (8.8, 12.5 and 16.2 psi). Drop the ball 5 times at each, from 2.00 m, measured to the bottom of the ball. Read each rebound height from the video.
- [ ] **Type the results** into a copy of `code/data/ball_drop_TEMPLATE.csv`, for example `my_ball_drops.csv`.
- [ ] **Run the analysis.** This makes Figure 2 and gives the numbers for Table 1:
  ```bash
  python ball_drop_analysis.py data/my_ball_drops.csv
  ```
- [ ] **Re-run the model** with the COR value the script prints, and note whether Figure 1 changes:
  ```bash
  python heading_impact_model.py --cor 0.83
  ```
- [ ] **Photograph your set-up** for the logbook.

**Rig concept and plan**
- [ ] **Sketch the rig on paper:** headform, neck, base, ball delivery, sensor position and speed measurement. Photograph the sketch; this is Figure 3.
- [ ] **Update the Gantt chart** if your supervisor suggests different dates. Edit the dates in `code/gantt_chart.py`, then run:
  ```bash
  python gantt_chart.py
  ```

## Stage 4: Write the first draft (by Mon 30 Nov)
Write the sections in this order, easiest first. Replace each yellow box with your own paragraph, then delete the slot label and the grey notes.

| Order | Section | Words | Done when |
|---|---|---|---|
| 1 | Preliminary work | ≈265 | Model, design implications, ball-drop results, rig concept and next steps all covered; Figures 1–3 and Table 1 mentioned in the text |
| 2 | Background and literature review | ≈410 | Six sub-sections; each key study has a finding *and* a limitation; ends with the research gap |
| 3 | Project plan, methodology and management | ≈165 | Methodology, resources (£75 budget), deliverables, management, risk / H&S / ethics / sustainability; Tables 2 and 3 mentioned |
| 4 | Introduction | ≈200 | Why, what and how; a one-sentence aim; 4–5 measurable objectives |
| 5 | Cover page | – | Every field filled in |

- [ ] Every number taken from a paper has a citation, for example [4].
- [ ] Use the past tense for work done ("A model was developed…") and the future tense for the plan ("The rig will be…").
- [ ] Keep to the word targets. About 1,050 words is what fits in 5 pages with the figures and tables (tested).
- [ ] Send the draft to your supervisor on Mon 30 Nov, if they agreed to read it.

## Stage 5: Figures and tables (by Wed 2 Dec)
- [ ] **Figure 1 (model):** already in the template.
- [ ] **Figure 2 (your ball-drop results):** put `figures/ball_drop_results.png` in the left box (Insert > Pictures).
- [ ] **Figure 3 (your sketch photo):** put it in the right box.
- [ ] **Table 1:** fill in COR mean, SD and contact time from the script's printout.
- [ ] **Table 2 (Gantt):** swap the picture if you changed the dates.
- [ ] **Table 3 (risks):** adapt it to your project and to your supervisor's advice.
- [ ] Every figure and table is numbered, has a caption, and is mentioned in the text ("as shown in Figure 1").
- [ ] Axis labels are readable when printed.
- [ ] **Never** use the example-data figure (it is stamped "EXAMPLE DATA, NOT REAL").

## Stage 6: References (by Wed 2 Dec)
- [ ] Delete the references you didn't cite, and renumber the rest in the order they first appear in your text.
- [ ] Check each reference's details against the paper itself. `references.md` marks with ⚠️ the ones that still need checking.
- [ ] Add "last accessed" dates to the web pages.
- [ ] Use the same format for every entry, following the template.
- [ ] Nothing copied: every sentence is in your own words. The module warns about plagiarism penalties.

## Stage 7: Final checks (by Wed 2 Dec)
**Required contents (from the module's "Preliminary Report Contents" slide)**
- [ ] **Introduction:** introduces the project: what you will do, why, aims and objectives.
- [ ] **Background and literature review:** what has been done before; shows your novel contribution; correct referencing.
- [ ] **Preliminary work:** what you have done to prepare for the main project.
- [ ] **Project plan:** methodologies, resources and deliverables; Gantt chart; expected activities; risk assessment; sustainability and health & safety; project-management procedures.
- [ ] **No more than 5 pages.**

**Tidy-up**
- [ ] Delete every grey ✎ note, slot label and the "How to use" box.
- [ ] Remove any leftover yellow highlight (select the text, then Home > Text Highlight Colour > No Colour).
- [ ] The page header shows your name, and the page numbers are there.
- [ ] Spell-check with English (UK) set (Review > Language).
- [ ] Read the whole report aloud once and fix anything clumsy.
- [ ] **5 pages or fewer, including the cover and references.** Check this in the PDF, not just in Word.
- [ ] Add an AI acknowledgement if the ECM3175 GenAI category requires it.

## Stage 8: Submit (Thu 3 Dec, one day early)
- [ ] **Make the PDF:** File > Save As, and choose PDF (or File > Export > Create PDF).
- [ ] **Check the PDF:** open it and look at every page, figure and table.
- [ ] **Check the size is under 15 MB.** If it isn't, use File > Compress Pictures in Word and export again.
- [ ] **Upload to the ECM3175 submission point on ELE.** The deadline is Fri 4 Dec at 12:00 noon.
- [ ] **Check you got the submission confirmation**, and screenshot it.
- [ ] If the upload fails, contact Harrison student services, not your supervisor or module leader.
- [ ] **Back up and log it:** save the final .docx and PDF in OneDrive and note the submission in your logbook.

**Afterwards:** Phase 1 of `4_full_project_plan.md` comes next (order parts, write the RAMS).
