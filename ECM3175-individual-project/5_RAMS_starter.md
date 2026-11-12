# RAMS starter: headform heading rig

This is a **starting point** for the official RAMS form (Risk Assessment + Method Statement). Copy the relevant parts into the form, then change them to match your real rig, room and equipment.
Your RAMS slides say "there is value in writing the documents yourself", and the technical staff can give you existing assessments to adapt.

Items in [square brackets] are for you to fill in. **No lab or workshop work can start until the module convenor has approved the RAMS.**

---

## Method Statement

**1. Project details:** [title, your name, supervisor, version number and date]

**2. Scope of work**
- **a. General description:** Design, build and test a rig that fires or drops a football at an instrumented headform (about 4.5 kg) mounted on interchangeable "necks". The aim is to measure head acceleration for different ball speeds (about 5–11 m/s), inflation pressures (0.6–1.1 atm) and neck stiffnesses. **No human participants.**
- **b. Equipment and tools** (add photos or sketches):
  1. headform (mannequin or 3D-printed shell, filled to 4.5 kg)
  2. neck elements (rubber blocks or springs)
  3. steel or aluminium base and frame
  4. ball delivery: [drop frame / pendulum / ball launcher]
  5. ADXL375 accelerometer
  6. [Arduino/ESP32] board and laptop
  7. size 5 footballs, pump with pressure gauge
  8. phone camera on a tripod, measuring scale
  9. hand tools; [workshop machines, with technician help]
  10. soldering iron and fume extractor
  11. [3D printer]
- **c. Materials and chemicals** (attach the safety data sheets, MSDS):
  1. solder and flux
  2. adhesive [epoxy / cyanoacrylate]
  3. headform filler [plaster / sand / water / gelatine]
  4. 3D-printing filament [PLA]
  5. water for the wet-ball tests

  **Each one needs a CoSHH form.**
- **d. Site planning and preparation:** [lab space agreed with the technical staff]. The test area needs a marked exclusion zone around the ball path. Store the rig and balls [where] between sessions. Keep water away from electronics.
- **e. Work method:**
  1. Check the area is clear and everyone present is wearing PPE.
  2. Set the ball pressure with the gauge.
  3. Start logging.
  4. Give a verbal countdown, then release the ball.
  5. Record the speed on video.
  6. Make the ball safe (catch it or let it come to rest), then stop logging.
  7. Save the data file and note it in the logbook.

  Maximum ball speed: 15 m/s. Maximum drop height: [x] m.

**3. Locations:** [lab name and room, building; workshop; electronics lab]

**4. Resources and support:**
1. workshop (cutting the frame), [technician name]
2. electronics lab (soldering), [name]
3. 3D printing, [name]
4. [ball launcher on loan from Sport and Health Sciences, if used]

Write: "Discussed with [names] on [dates]."

**5. Safety rules:**
- **a. Inductions:** [workshop, electronics lab, 3D printer, test lab], with dates.
- **b. Local rules:** [list each lab's rules]

**6. Organisation, responsibilities and supervision:**
- Student: [you]
- Academic supervisor: [name]
- Safety supervisor / technical staff: [name]

No lone working: tests only happen during staffed hours, with a second person present for drop or launch tests.

**7. Referenced documents:**
1. this risk assessment
2. CoSHH forms (flux, adhesive, filler)
3. equipment inductions
4. [launcher operating instructions]

**8. Decommissioning:** Take the rig apart, return borrowed equipment, dispose of filler and waste correctly, recycle electronics or keep them for reuse, and clean the area. Time needed: about 1 day (planned 29 Mar – 2 Apr 2027).

**9. Schedules** (location, activity, how often and how long):
- [workshop] frame build, 4 × 3 h (Jan)
- [electronics lab] soldering, 2 × 2 h (Jan)
- [test lab] calibration and validation, 6 × 3 h (Feb)
- [test lab] main tests, 8 × 3 h (late Feb – mid Mar)
- [test lab] decommissioning, 1 × 6 h (end of Mar)

**10. Significant dates:** [inductions], RAMS approval target 15 Jan 2027, [launcher collection or return], tests 22 Feb – 19 Mar 2027.

**11. Contacts:** student, supervisor, technical staff (University email addresses).

**12. Emergency procedures:** [evacuation route and assembly point for each lab]. First aid: [first-aider names and how to contact them]. Aware of emergency procedures: Y/N.

**13. Amendments:** record every change, for example "v2: switched from drop to launcher".

**14. Briefing:** everyone involved signs to confirm they have read the method statement.

---

## Risk Assessment

Check the numbers against **tables 1a, 1b and 1c on the official form**:
- Consequence (C) is scored **without** controls.
- Likelihood (L) is scored **with** controls, and should be 1–2.
- Score = C × L. The final score must be **GREEN**.

| Ref | Hazard | Who could be harmed | How | Control measures (be specific) | C | L | Score |
|---|---|---|---|---|---|---|---|
| A | Ball moving at up to 15 m/s (launcher, pendulum or drop) | Student, others nearby | Blow to the face or eyes | Safety glasses to BS EN 166; marked exclusion zone; net or barrier behind the headform; verbal countdown; launch only when the zone is clear; speed limit 15 m/s; launcher used only after training | 3 | 1 | 3 |
| B | Falling objects from the drop frame (ball, release, headform if the mount fails) | Student, others | Impact injury to the head or feet | Never stand or reach under the drop path; mounts checked before each session; safety shoes to EN ISO 20345 S3 if heavy parts are overhead; frame clamped or bolted to the floor or bench | 3 | 1 | 3 |
| C | Moving parts: pendulum arm, release mechanism, neck flexing | Student | Trapped or crushed fingers | Hands clear before release; guard around the pendulum swing; release mechanism locked while loading | 3 | 1 | 3 |
| D | Lifting the heavy base or "torso" mass (20–30 kg) | Student | Back strain, crushed feet | Two-person lift or trolley; keep low; split the mass into smaller plates; safety shoes | 3 | 1 | 3 |
| E | Workshop tools and machines (saw, drill) | Student | Cuts, entanglement, flying chips | Workshop induction; technician present; machine guards; safety glasses BS EN 166; cut-resistant gloves to EN 388 for hand tools (**not** on rotating machines); no loose clothing | 4 | 1 | 4 |
| F | Soldering | Student | Burns, flux fumes | Electronics lab induction; fume extractor; heat-resistant mat and stand; CoSHH for flux; wash hands after | 2 | 1 | 2 |
| G | Electrics (USB or low-voltage battery) | Student | Minor shock, battery fire | USB / low-voltage only, no mains wiring; PAT-tested laptop and chargers; no lithium-polymer batteries (or a fire-safe bag if they're essential) | 2 | 1 | 2 |
| H | 3D printing | Student | Burns from the hot nozzle or bed, fumes | 3D printer induction; ventilated room; don't touch parts until cool | 2 | 1 | 2 |
| I | Water from the wet-ball tests | Student, others | Slips; water on electronics | Soak balls in a tray away from the rig; absorbent mat; wipe the floor straight away; "wet floor" sign; electronics kept above and away | 2 | 1 | 2 |
| J | Headform filler (plaster dust / gelatine) | Student | Breathing in dust; skin irritation | Mix in a ventilated area; dust mask to FFP2 if dusty; nitrile gloves; CoSHH form | 2 | 1 | 2 |
| K | Lone working | Student | Delayed help after an accident | Staffed hours only; technician knows when testing is happening; second person present for launch or drop tests | 3 | 1 | 3 |
| L | Over-inflating the ball | Student | Ball bursts (noise, minor impact) | Pump only to 1.1 atm (Law 2 maximum), checked with the gauge | 2 | 1 | 2 |

**Tips from your RAMS slides:**
- List *everything*, including the obvious things.
- If you name a standard, make sure your equipment meets it.
- Keep records of training and of who has read the documents.
- Schedule and record reviews.
- Update the Amendments section whenever the method changes.
