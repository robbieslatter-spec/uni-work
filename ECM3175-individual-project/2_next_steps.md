# Next steps: from today to the preliminary report (Fri 4 December 2026, 12 noon)

## Key dates (from your module slides)
| Date | What | Notes |
|---|---|---|
| **Fri 4 Dec 2026, 12:00** | Preliminary report (max 5 pages) | Upload as a PDF to ELE. Size limit 15 MB, so shrink photos. |
| Mon 3 May 2027, 12:00 | Final report (35 pages) | 90% of the module mark |
| 19–28 May 2027 | Interview with supervisor and examiner | 10% of the module mark |

---

## Week 1: Thu 12 to Fri 20 Nov (decide and get started)
- [ ] **Email your supervisor today.** A draft email is below. Ask for a meeting this week.
- [ ] **Start your logbook.** Use a notebook or a OneNote/Word file, and date every entry. Record ideas, meetings, sources, calculations and test results. The slides ask for this, and it helps a lot in the interview.
- [ ] **Read the five key papers:** [1], [4] and [5] in full; skim [2] and [8]. For each, note what they did, what they found and what they missed.
- [ ] **Run the code** (see `README.md`) and look at the figures. Make sure you can explain each figure in one sentence.
- [ ] **Buy a ball pump with a pressure gauge** (about £10–20). Have a size 5 football ready.
- [ ] **Check the AI rules for ECM3175 on ELE.** Exeter uses four categories: AI-integrated, AI-assisted, AI-minimal and AI-prohibited. Find out which one applies before you use any AI-written text, and acknowledge AI help if the rules ask you to.

## Week 2: Sat 21 to Fri 27 Nov (preliminary work)
- [ ] **Do the ball-drop experiment.** It takes about an hour; the method is at the top of `code/ball_drop_analysis.py`. Use pressures of 0.6, 0.85 and 1.1 atm, with 5 drops each from 2.0 m.
- [ ] **Analyse your data:**
  ```bash
  python ball_drop_analysis.py data/my_ball_drops.csv
  ```
  Then re-run the model with your measured value:
  ```bash
  python heading_impact_model.py --cor 0.83
  ```
  Replace 0.83 with the COR the first script prints.
- [ ] **Sketch the rig concept** (a hand sketch or simple CAD is fine). Show the head, neck, base, ball delivery and sensor position.
- [ ] **Meet your supervisor.** Use the questions below. Confirm the project title and scope.
- [ ] **Keep reading** and add notes to your logbook. Aim for about 12–15 references in the report.

## Week 3: Sat 28 Nov to Thu 3 Dec (write and submit)
- [ ] **Write the report** using `3_preliminary_report_OUTLINE.docx`. Turn the bullet points into your own paragraphs, and stay within 5 pages.
- [ ] **Insert your figures:** the model figure, your ball-drop results, your rig sketch and the Gantt chart.
- [ ] **Check every reference** against the original paper (see the notes in `references.md`).
- [ ] **Ask your supervisor** if they will look at a draft. Many will glance at it if you send it 3–4 days early.
- [ ] **Export to PDF.** Check it is 5 pages or fewer and under 15 MB.
- [ ] **Submit on Thu 3 Dec**, one day early, so an upload problem doesn't make you late. For submission problems contact Harrison student services, not your supervisor.

---

## Draft email to your supervisor
> **Subject:** ECM3175 project "Sport Injury Biomechanics": meeting request
>
> Dear [supervisor name],
>
> I am [your name], and I have been allocated the "Sport Injury Biomechanics" project. I would like to propose a focus on football heading: designing and building an instrumented headform rig to measure how ball speed, inflation pressure and neck stiffness affect head acceleration, supported by a mathematical impact model that I have started. As a backup, I have also looked at running-shoe midsole degradation.
>
> Could we meet this week or early next week to agree the scope before the preliminary report deadline on 4 December? I would also like to ask what equipment is available (for example a headform, ball launcher, high-speed camera or accelerometers).
>
> Many thanks,
> [your name], [programme], [student number]

## Questions for your first supervisor meeting
1. Is the heading-rig direction a good fit for the "Sport Injury Biomechanics" title? Would you prefer a different emphasis?
2. What equipment can I use? For example: a Hybrid III or other headform, a ball launcher (perhaps from Sport and Health Sciences), a high-speed camera, a force plate, accelerometers or a data-acquisition system, a drop tower, an Instron, 3D printers, the workshop.
3. Is there a budget for parts (about £50–150 for a sensor, microcontroller and materials)? How do I order through the department?
4. Ethics: with no human participants, do I still need to fill in an ethics self-assessment form?
5. Which GenAI category applies to ECM3175, and how should I acknowledge AI tools?
6. Who are the technicians, and which lab inductions or risk assessments do I need before building and testing?
7. When should we meet each week?

---

## Kit list for the recommended project
Prices are rough guides only, so check suppliers. Ask the department first: they may already own it.

| Item | Purpose | Approx. cost |
|---|---|---|
| ADXL375 ±200 g accelerometer breakout | Measures head acceleration | £20–35 |
| ESP32 / Arduino / Teensy board + microSD module | Logs data at 3.2 kHz | £15–40 |
| Mannequin head (or 3D-printed shell) + filler | Headform of about 4.5 kg | £15–40 |
| Rubber blocks / springs (2–3 stiffnesses) | Swappable "necks" | £10–30 |
| Frame materials (aluminium extrusion, MDF) | Base, torso mass, drop or pendulum frame | workshop |
| Football ×2, pump with gauge | Test balls, pressure control | £30–60 |
| Replica vintage leather ball (extension) | U1 tests | £30–60 |
| Phone with 240 fps slow-motion | Ball speed and contact checks | (own) |

## Risks (also needed in the report)
| Risk | Likelihood | Impact | What you'll do about it |
|---|---|---|---|
| Rig takes longer to build than planned | Medium | High | Simple first version (drop rig) by early Feb; upgrade later only if time allows |
| Sensor or electronics don't work / saturate | Medium | High | Bench-test the sensor in December; model shows peaks under 60 g, so ±200 g leaves a big margin; spare sensor |
| Ball speed not repeatable | Medium | Medium | Use drop or pendulum (gravity-driven, repeatable); measure every speed on video |
| No access to a ball launcher / headform | Medium | Medium | Gravity-driven delivery; home-made headform |
| Results don't match the model | Medium | Low | This is still a finding: explain why and refine the model |
| Illness or other deadlines | Low | Medium | Two-week buffer in the Gantt chart; weekly meetings catch slippage early |
| Data loss | Low | High | Code and data on GitHub plus OneDrive; logbook |

**Health and safety:** flying balls (eye protection, keep clear of the launch path); falling masses on drop rigs (guarding, never put hands under the mass); pinch points; lifting heavy torso masses; low-voltage electronics only; complete the lab inductions and the department risk assessment before testing.

**Sustainability:** reuse balls and existing lab equipment; use reclaimed or 3D-printed parts where possible; low-power electronics. For the shoe project, extending shoe life cuts waste.

**Ethics:** no human participants in the recommended project. Confirm with your supervisor whether a self-assessment form is still needed. The wearable shoe idea (2C) *would* need full ethics approval.
