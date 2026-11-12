# Full project plan: ECM3175 Individual Project (Nov 2026 to May 2027)

**Project:** *Sport Injury Biomechanics: an instrumented headform study of how ball speed, inflation pressure and neck coupling affect head acceleration in football heading.*

This plan is built from your uploads: the module slides, the marking criteria, the RAMS presentation, the budget and ordering rules, the final report rules, and the 11 example final reports.
The chart is in `figures/gantt_chart.png`. Edit `code/gantt_chart.py` to change it.

---

## 1. The rules you must not break

| Rule | Source | What it means for you |
|---|---|---|
| **Preliminary report: Fri 4 Dec 2026, 12:00**, max 5 pages, PDF to ELE, 15 MB limit | Slides | Submit on Thu 3 Dec, one day early |
| **No lab or workshop work until your RAMS is approved** (supervisor, then module convenor) | RAMS slides | Write it in early December so approval comes through by mid-January |
| **Budget £75.** Order only through the Order Form (Preferred Suppliers List) to engstudentordering@exeter.ac.uk | Budget page | **Never buy parts yourself, because you won't be reimbursed.** You can't top up an overspend with your own money. Agree every purchase with your supervisor first |
| Extra funding from sponsors is allowed if you justify it | Budget page | You could ask a club, retailer or manufacturer to donate a ball. Report it |
| All money matters go in the final report | Budget page | Keep a spending log from day one |
| **Final report: Mon 3 May 2027, 12:00**, **max 35 A4 pages INCLUDING cover, abstract, contents, references, appendices and Gantt**. Pages after 35 are not marked | Final report page | Use the official final-report template from ELE (it fixes font, margins and spacing). Put code on GitHub instead of in appendices |
| Final report = **90%**, interview (19–28 May) = **10%** | Slides | Plan time for the interview too |
| GenAI rules: one of four categories (integrated, assisted, minimal, prohibited) | University policy | Check the ECM3175 category on ELE before using AI for anything you submit |

> 3 May 2027 is the early May bank holiday. **Submit by Fri 30 April.**

---

## 2. Where the marks are, and how this project will earn them

| Section (marks) | "Excellent" needs | How you'll get it |
|---|---|---|
| **Abstract (5)** | Background, aim, methods, main outcomes, conclusions, written concisely | Write it **last**, 250–300 words, with real numbers in it |
| **Introduction & background (5)** | Clear what, why and how; precise aim and objectives | Reuse and sharpen the preliminary report introduction |
| **Literature review (15)** | Wide range, critical (not just descriptive), accurate referencing, **recent advances**. Must be **updated and expanded** from the preliminary report | 30–40 sources including 2023–2026 papers. For each paper say what it adds *and* what it misses, then end with the gap |
| **Methodology & theory (20)** | Deep understanding of the theory, originality, clear progress beyond background reading | Derive the impact model properly (membrane contact, adiabatic air, Hunt–Crossley damping, neck coupling, RK4), add a sensitivity study, and justify the rig design from the model |
| **Experimental work / design (20)** | Clear description; collect and interpret data **with autonomy** | CAD, build, calibration, validation, step-by-step test procedure, plus the problems you solved |
| **Results (15)** | Neat, self-explanatory plots and tables, clearly labelled and referenced in the text | Same plotting style throughout; every figure has a one-sentence takeaway; means ± SD |
| **Discussion & conclusions (10)** | New knowledge, compared with the literature, foundations for future work, "publishable" | Answer each objective, compare with [4], [5] and [6–8], state limitations honestly, give specific future work |
| **Project management, sustainability, ethics, IP, H&S, English (10)** | Clear management system, H&S and ethics awareness, commercial and IP awareness, sustainability, very good English | Planned-vs-actual Gantt, budget table, RAMS summary, ethics, sustainability, IP/commercial section, proofreading |

**40% of the marks are Methodology + Experimental work.** That is where the effort goes.

---

## 3. Final report blueprint (35 pages in total)

Every example report you uploaded uses the same 7 numbered chapters, matching the marking sections, plus an abstract with keywords, a contents page and references. Copy that structure.

| Part | Pages | ≈ Words | Contents for *this* project |
|---|---|---|---|
| Cover, abstract + keywords, contents | 3 | 300 | Use the template cover. Abstract last |
| 1 Introduction & background | 2 | 600 | Why (dementia evidence, FA rules), problem, how, aim, objectives O1–O5, report layout |
| 2 Literature review | 5.5 | 1,800 | 2.1 heading and brain health · 2.2 heading biomechanics · 2.3 injury measures (linear/rotational, HIC) · 2.4 ball properties and Law 2 · 2.5 neck strength and coupling · 2.6 test methods (headforms, sensors, mouthguards) · 2.7 gap and hypotheses |
| 3 Methodology & theory | 5.5 | 1,700 | 3.1 approach · 3.2 impact model equations · 3.3 calibration (ball drop) and sensitivity · 3.4 rig requirements and concept choice (decision matrix) · 3.5 test matrix and statistics |
| 4 Experimental work & design | 6 | 1,500 | 4.1 CAD design · 4.2 build (photos) · 4.3 electronics and software · 4.4 calibration · 4.5 validation · 4.6 test procedure · 4.7 problems and fixes |
| 5 Results | 5 | 1,000 | Validation, then speed, pressure and neck effects; extension; model vs experiment |
| 6 Discussion & conclusions | 3 | 1,000 | Meaning, comparison with literature, limitations, recommendations, future work, numbered conclusions |
| 7 Project management, sustainability, ethics, IP, H&S | 2.5 | 800 | Management system, planned vs actual Gantt, budget table, RAMS summary, ethics, sustainability, IP/commercial |
| References | 2.5 | ~35 refs | One consistent numbered style |
| Appendices | 0 | – | Link to your GitHub repository instead |
| **Total** | **35** | **≈8,700** | Examples: 28–37 pages, about 6,000–11,500 words, 2–27 figures |

**Lessons from the example reports:**
- **Don't paste equations as images.** One abstract *apologised* for equations that pasted badly. Use Word's equation editor in the official template from day one.
- **Pilot your test method early.** One project found its sample preparation and alignment were flawed only at the end, so its results were "very spread".
- **Plan enough repeats and some statistics.** One project reported "inconclusive data".
- **Itemise your spending.** The boot-stud example (Manufacturing.2) has a "Financial Awareness" section listing every cost against the budget. Do the same.
- **Stud traction has already been done here.** The same boot-stud report tested stud torque at Exeter, so the traction-tester idea is not new. This is another reason to choose the headform rig.
- **Copy Mechanical.3's structure.** It validates a model against experiments, exactly like yours.

---

## 4. Phases and gates

| Phase | Dates | Goal | Gate (must be true to move on) |
|---|---|---|---|
| 0. Start and preliminary report | 12 Nov – 4 Dec | Scope agreed, preliminary work done, report submitted | **G0:** report submitted (Thu 3 Dec) |
| 1. Design, RAMS, ordering | 5 Dec – 10 Jan | Rig designed, parts ordered, RAMS with supervisor | **G1 (Fri 18 Dec):** order sent, RAMS with supervisor |
| 2. Build and bench test | 11 Jan – 5 Feb | Rig built, sensor logging | **G2 (Fri 29 Jan):** sensor logs at ≥3 kHz on the bench (checked with timestamps) |
| 3. Calibrate and validate | 1 – 19 Feb | Rig is trustworthy | **G3 (Fri 19 Feb):** 10 repeat impacts with ≤10% variation (CV); ball speed within ±0.5 m/s; results within ~30% of the model and literature |
| 4. Main tests | 22 Feb – 19 Mar | Full test matrix done | **G4 (Fri 19 Mar):** all data collected and backed up |
| 5. Analysis | 1 Mar – 2 Apr | Results, statistics, refined model | Results figures final |
| 6. Writing and submission | Jan – 30 Apr (as you go) | Report finished | **G5 (Fri 9 Apr):** full draft to supervisor · **G6 (Fri 30 Apr):** submitted |
| 7. Interview | 4 – 28 May | Ready to defend the work | Practice run done |

**If a gate is missed:** tell your supervisor that week, then cut scope in this order:
1. The extension (leather ball).
2. The third neck stiffness.
3. Three speeds down to two.

**Never cut validation or writing time.**

---

## 5. Week-by-week plan

### Phase 0: Start and preliminary report
**Week 0 (Thu 12 – Sun 15 Nov)**
- [ ] Email your supervisor and ask for a meeting (draft in `2_next_steps.md`).
- [ ] Start your logbook and date every entry.
- [ ] Read [1], [4] and [5] properly. Run the code in `code/`.

**Week 1 (16 – 22 Nov)**
- [ ] **Supervisor meeting 1:**
  - agree the scope and title
  - ask what equipment exists (headform, launcher, Arduinos, DAQ, high-speed camera)
  - ask about lab space, the AI category, and whether ethics needs a self-assessment form
  - check the £75 budget plan
- [ ] Do the **ball-drop experiment.** Your own ball and pump are fine for this, because you're not claiming money. Run `ball_drop_analysis.py`.
- [ ] Find the lab manager or technical staff and ask which inductions you'll need. This is RAMS step 1.

**Week 2 (23 – 29 Nov)**
- [ ] Draft the preliminary report from `3_preliminary_report_OUTLINE.docx` in your own words.
- [ ] Sketch rig concepts (drop, pendulum, launcher) and add your sketch to the report.
- [ ] Send the draft to your supervisor by about Thu 26 Nov if they've offered feedback.

**Week 3 (30 Nov – 4 Dec)**
- [ ] Finalise the report, check it is 5 pages or fewer and under 15 MB, and **submit Thu 3 Dec.**

### Phase 1: Design, RAMS, ordering (keep it light over Christmas)
**Week 4 (7 – 13 Dec)**
- [ ] Choose parts from the **Preferred Suppliers List** (see section 6) and agree them with your supervisor.
- [ ] Email the **Order Form** to engstudentordering@exeter.ac.uk.
- [ ] Meet the technical staff to discuss space, storage, inductions and how to build the frame.
- [ ] Start the CAD (headform mount, neck, base, ball delivery).

**Week 5 (14 – 20 Dec)**
- [ ] **Write the RAMS:**
  - Method Statement sections 2–14
  - Risk Assessment
  - CoSHH forms for solder flux, adhesives and any filler
  - Use `5_RAMS_starter.md` as your starting point.
- [ ] **Send the RAMS to your supervisor by Wed 16 Dec.**
- [ ] Finish the CAD. Write the test matrix (section 7).
- [ ] Run a sensitivity study on the model: how much do head mass, forehead radius and COR change the results?

**Christmas vacation (21 Dec – 10 Jan): low-pressure tasks you can do at home**
- [ ] **Write the literature review chapter.** Expand to 30+ sources and include recent (2023–2026) work.
- [ ] Download the **final report template** from ELE and set up chapters 1–7 in it.
- [ ] Write the Arduino/ESP32 logging code and the analysis script. This is software only, so no RAMS is needed.
- [ ] Chase the order and RAMS approval in the first week of January if you've heard nothing.

### Phase 2: Build (Term 2 starts Mon 11 Jan)
**Week 6 (11 – 17 Jan)**
- [ ] Complete your inductions. Collect the parts.
- [ ] Bench-test the sensor: verify the sample rate and run a static ±1 g check.
- [ ] **RAMS approved (target Fri 15 Jan)**, then start lab work.

**Week 7 (18 – 24 Jan)**
- [ ] Build the headform to 4.5 kg ± 0.1 kg and find its centre of mass. Mount the sensor there.
- [ ] Make the neck elements. Measure each one's stiffness with a static load test.

**Week 8 (25 – 31 Jan)**
- [ ] Build the ball delivery and set up speed measurement (slow-motion video with a scale).
- [ ] **G2 (Fri 29 Jan):** logging at ≥3 kHz works.

### Phase 3: Calibrate and validate
**Week 9 (1 – 7 Feb)**
- [ ] Run the first impacts and debug.
- [ ] Calibrate: accelerometer, headform mass, neck stiffness, speed measurement.
- [ ] Draft the **Methodology & theory chapter.**

**Week 10 (8 – 14 Feb)**
- [ ] Repeatability test: 10 impacts at one setting.
- [ ] Compare with the model and with [4]. Recalibrate the model.

**Week 11 (15 – 21 Feb)**
- [ ] Run a pilot of the full procedure. Fix the test order (randomise it).
- [ ] **G3 (Fri 19 Feb): rig validated.**

### Phase 4: Main tests
**Week 12 (22 – 28 Feb)**
- [ ] Neck A: 3 pressures × 3 speeds × 5 repeats = 45 impacts. Back up the data the same day.

**Week 13 (1 – 7 Mar)**
- [ ] Neck B: 45 impacts.
- [ ] Start the analysis scripts on real data.
- [ ] Start the **Experimental work chapter.**

**Week 14 (8 – 14 Mar)**
- [ ] Neck C (optional).
- [ ] **Extension:** dry vs soaked leather ball vs modern ball, but only if the budget or a sponsor allows.

**Week 15 (15 – 21 Mar)**
- [ ] Re-test any gaps.
- [ ] **G4 (Fri 19 Mar): all data collected.**
- [ ] Finish the Experimental work chapter.

### Phase 5–6: Analysis and writing
**Week 16 (22 – 28 Mar)**
- [ ] Statistics: regression or two-way ANOVA of peak acceleration against speed and pressure; neck effect; uncertainty.
- [ ] Fit the model's neck parameters. Finalise the results figures.

**Week 17 (29 Mar – 4 Apr)**
- [ ] **Decommission:** take the rig apart, return borrowed kit, tidy and clean the space. This is RAMS section 8.
- [ ] Write the **Results** chapter.

**Week 18 (5 – 11 Apr)**
- [ ] Write the **Discussion & conclusions**, then **Chapter 7** (management, sustainability and the rest), then the **abstract.**
- [ ] **G5 (Fri 9 Apr): full draft to supervisor.**

**Week 19 (12 – 18 Apr)**
- [ ] Act on the supervisor's feedback.

**Week 20 (19 – 25 Apr)**
- [ ] Check every reference against its source.
- [ ] Make figures consistent.
- [ ] Proofread aloud.
- [ ] **Count pages: 35 or fewer, including everything.**

**Week 21 (26 Apr – 2 May)**
- [ ] Final read-through. Export the PDF and check it.
- [ ] **Submit Fri 30 Apr.** (Deadline is Mon 3 May, 12:00.)

### Phase 7: Interview (10%)
**Weeks 22–23 (3 – 16 May)**
- [ ] Find out the interview format on ELE.
- [ ] Prepare a 2-minute and a 5-minute summary.
- [ ] Prepare photos and video of the rig, and bring your logbook.
- [ ] Practise the questions below with a friend.

**Weeks 24–25 (17 – 28 May)**
- [ ] Interview.

**Likely interview questions:**
- Why this approach?
- Why model the ball as a membrane? What does Hunt–Crossley damping do?
- How do you know your rig is accurate?
- How do your results compare with Naunheim and Shewchenko?
- What are the biggest limitations?
- What would you do differently?
- How could this reduce brain injury risk in practice?
- How did you manage risk, budget and sustainability?

---

## 6. Budget plan (£75, ordered through the department)

These prices are rough guides. Check the real prices on the Preferred Suppliers List, and agree everything with your supervisor *before* ordering.

| Priority | Item | Est. cost | Notes |
|---|---|---|---|
| Essential | ADXL375 ±200 g accelerometer breakout | £20–30 | Core sensor. Model peaks are under 60 g, so ±200 g gives a big safety margin |
| Essential | Microcontroller (Arduino or ESP32) | £0–25 | **Ask to borrow one** from teaching-lab stock first |
| Essential | microSD module + card | £0–10 | Or stream data over USB to a laptop for £0 |
| Essential | Neck elements (rubber blocks or springs, 2–3 stiffnesses) | £10–15 | |
| Essential | Ball pump with pressure gauge | £5–10 | |
| Essential | Headform (mannequin head or 3D print) + filler to 4.5 kg | £10–15 | Ask whether workshop stock and departmental 3D printing are free |
| Borrow | Footballs ×2 | £0 | Sports department, a club, or your own |
| Optional | Replica vintage leather ball (extension) | £30–60 | Only if money is left, your supervisor agrees, or a sponsor donates one |
| | **Target spend** | **≤ £65** | Keeps about £10 in reserve |

**Process:**
1. Make your list and get your supervisor's OK.
2. Fill in the Order Form using the Preferred Suppliers List and email it to engstudentordering@exeter.ac.uk. Read the "Student Project Ordering Process: Student Notice" first.
3. Log each item, its price and its delivery date in a spending table. This becomes the budget table in Chapter 7.

---

## 7. Test matrix and data handling

- **Factors:**
  - **Speed:** 3 levels, for example about 5, 8 and 11 m/s. A 5 m drop gives about 10 m/s. Your final levels depend on the delivery method.
  - **Pressure:** 3 levels: 0.6, 0.85 and 1.1 atm (the Law 2 range).
  - **Neck stiffness:** 2–3 levels.
  - **Repeats:** 5 per condition.
- **Size:** 90–135 impacts, plus 10 repeatability impacts and the extension.
- **Test order:** randomise it within each neck setup, so drift (ball warming up, rig loosening) doesn't bias the results.
- **Measured for every impact:** peak linear acceleration (g), contact time (ms), HIC15, ball speed (video), ball pressure (checked every 10 impacts), room temperature.
- **Data handling:**
  - one CSV per session, with a clear name such as `2027-02-23_neckA_session1.csv`
  - **never edit raw files**; all processing happens in Python scripts
  - push to GitHub and copy to OneDrive the same day
  - photograph the setup every session for the report

---

## 8. RAMS (risk assessment + method statement)

The approval route, from your RAMS slides:
1. **Talk to the lab manager or technical staff:** inductions, risk advice, space. Record this in section 4 of the method statement.
2. **You write the Method Statement and the Risk Assessment.**
3. **Your supervisor checks them** and decides whether you can work alone after training or need close supervision.
4. **The module convenor checks them with the technical staff.** There may be one round of changes and a panel review. **Only then can lab work start.**
5. The Head of Department is involved only if the work is contentious.

Rules from the slides:
- **Risk score = consequence (scored without controls) × likelihood (scored with controls).** The final score must be **GREEN**.
- Likelihood should be **1–2**.
- Control measures must be **specific**: for example "safety glasses to BS EN 166", not just "glasses".
- Any substance (solder flux, glue, resin, plaster) needs a separate **CoSHH** form.
- When your method changes, update the **Amendments** section and keep records of training.

Starter content is in [`5_RAMS_starter.md`](5_RAMS_starter.md).

**You *can* do these before approval:** CAD, coding, the model, reading, writing and ordering. **You *can't* do these:** any lab or workshop building or testing.

---

## 9. Project management system (this earns marks in Chapter 7)

- **Weekly:**
  - **Monday (15 min):** check the Gantt and pick 3 goals for the week.
  - **Supervisor meeting (30 min):** send a short agenda and progress note 24 hours before; write the actions in your logbook.
  - **Friday (15 min):** back up (git push + OneDrive) and log progress against the plan.
- **Time:** block 2–3 fixed sessions a week, roughly 8–12 hours. Allow more in testing weeks (Feb–Mar).
- **Logbook:** meetings, decisions, calculations, test settings, problems, photos. Your supervisor and the interviewers will value it.
- **Gantt:** keep the original chart and update an "actual" version every two weeks. Show **both** in the final report and explain the differences.
- **Writing as you go:** two 1-hour writing sessions a week from January, so no chapter starts from a blank page in April.
- **References:** use a reference manager (Zotero or Mendeley) with one numbered style from the start.

---

## 10. Covering the "10 marks" section (Chapter 7)

- [ ] **Management:** your system (section 9), planned vs actual Gantt, what slipped and how you recovered.
- [ ] **Financial:** itemised spending against £75, including donated or borrowed items.
- [ ] **Health & safety:** RAMS summary, inductions completed, main hazards and controls, incidents (hopefully none).
- [ ] **Ethics:** no human participants. Say why you chose a surrogate (safety, repeatability, no ethics delay) and confirm any self-assessment your supervisor required.
- [ ] **Sustainability:**
  - environmental: reused or borrowed kit, low-power electronics, waste from the rig, life cycle of a synthetic football
  - social: player brain health, UN Sustainable Development Goal 3 (good health and well-being)
- [ ] **Commercial & IP:**
  - who might use a low-cost heading test rig (grassroots clubs, ball makers, researchers)
  - existing products (instrumented mouthguards, headgear)
  - the University's IP policy for student work
  - a licence for your code (for example MIT)
- [ ] **English:** proofread. Check whether grammar tools count as GenAI under the ECM3175 category.

---

## 11. Risks to the plan

| Risk | Early warning | Response |
|---|---|---|
| RAMS approval late | No reply by 8 Jan | Chase the supervisor, then the convenor. Do code and writing meanwhile |
| Parts late or wrong | Not delivered by 11 Jan | Borrow departmental kit. Simplify (stream over USB) |
| Rig repeatability poor | CV > 10% at G3 | Switch to gravity drop, clamp the ball release, add more repeats |
| Sensor problems | G2 missed | Lab DAQ + analogue accelerometer from the technical staff, or lower speeds |
| Results far from the model | Big mismatch at G3 | Still publishable: investigate (mass, contact, filtering), then refine the model |
| Falling behind | Gate missed | Cut scope in the order in section 4 and tell your supervisor |
| Illness or other deadlines | – | Two-week buffer (draft 9 Apr, deadline 3 May). Apply for mitigation if needed |
| Data loss | – | Daily git push + OneDrive |
