# Project ideas: Sport Injury Biomechanics (ECM3175)

This file covers your two ideas made more "engineering", three new ideas, a comparison and my recommendation.
Numbers in [square brackets] refer to the papers in [`references.md`](references.md).

---

## The main improvement: turn "X causes injury" into an engineering question

As you've stated them, "heading causes brain injury" and "shoes cause running injuries" are really **medical** questions. To answer them properly you would need thousands of people followed for years, which is impossible in one project. Any study that uses people also needs ethics approval, and that takes weeks.

An engineering project instead **measures, models and improves the mechanics** that sit between the activity and the injury:

| Medical question (too big for one project) | Engineering question (doable and measurable) |
|---|---|
| Does heading cause dementia? | What controls how hard the head is accelerated in a header, and which engineering changes reduce it? |
| Do running shoes cause injuries? | How quickly does midsole foam lose its cushioning, and how does that change the loads on a runner? |

Using a **test rig or mechanical surrogate instead of people** has four advantages:

- No ethics delay.
- Repeatable tests.
- Real engineering content: design, build, sensors and modelling.
- A clear "novel contribution", which the module slides ask for.

---

## Your idea 1: heading in football

### Why it is a strong topic
- **The health concern is real.** Former Scottish professional footballers were about 3.5 times more likely than matched controls to die with neurodegenerative disease (1.7% vs 0.5%) [1].
- **Heading looks like the cause.** Goalkeepers, who rarely head the ball, did **not** have the raised risk. Defenders had the highest risk, about 5 times that of controls [2].
- **The problem is repetition, not single headers.** One header gives only about 16 g (ball at 9 m/s) to 20 g (12 m/s) of head acceleration, far below concussion levels [4]. The concern is repeated "sub-concussive" impacts: one routine heading session caused measurable short-term changes in brain function and memory [3].
- **It is live policy.** Since 2021, English guidance has recommended a maximum of 10 "higher-force" headers per week in professional training [10]. The FA is phasing out deliberate heading in U7 to U11 matches, finishing in 2026/27 [11].
- **The literature already hints at engineering levers.** Halving ball pressure reduced head response by about 10–31% [5]. Stronger necks are linked to lower head acceleration [6, 7, 8].

### Improved versions
**1A. Instrumented headform rig (recommended).** Design, build and validate a low-cost "robot head": a headform on an adjustable neck with a ±200 g accelerometer inside. Use it to measure how **ball speed, inflation pressure and neck stiffness** change head acceleration, and back it up with a computer model. The model is already started in `code/heading_impact_model.py`.
- *Engineering content:* mechanical design and CAD, sensors and electronics, signal processing, impact dynamics, experimental validation.
- *No human participants*, so no ethics delay.

**1B. Computer model only.** A finite-element model in ANSYS of a pressurised football hitting a head, validated with ball-drop tests. It needs little equipment, but it is less hands-on and harder for a beginner.

**1C. Does football headgear work?** Test soft heading headbands on the 1A rig. This makes a good extra chapter but is too small on its own.

---

## Your idea 2: running shoes and injury

### What the literature says
- **Injuries are common.** Depending on the study, about 19% to 79% of distance runners get injured [16].
- **Whether shoes cause injuries is disputed.**
  - Nigg et al. argue the evidence that impact forces or pronation cause injuries is weak [17].
  - A prospective study found that injured female runners who needed medical care had higher loading rates. Above 66 body weights per second (BW/s), the odds of injury were about 2.7 times higher [18].
  - In a randomised trial with 848 runners, harder shoes (95 vs 61 N/mm) increased injury risk, but only in lighter runners [19].
- **Shoes wear out.**
  - Shoes lost much of their shock absorption within a few hundred miles [20].
  - Peak heel pressure doubled after 500 km, and the EVA foam was visibly damaged after 750 km [21].
  - Runners partly adapt their technique to worn shoes [22].
- **Measure the right thing.** The usual "impact peak" is not a valid measure of cushioning, so measure the high-frequency part of the impact instead [23].
- **"Super-shoes" are a research gap.** Shoes with new foams save about 4% energy [25], but much less is known about how long their foam lasts.

### Improved versions
**2A. How fast do running shoes lose their cushioning? EVA vs "super-shoe" foam (strong backup).**
- Build an ASTM F1976-style drop tester (8.5 kg striker, about 5 J) [26].
- Test new and worn shoes: donated shoes with known distance, plus new shoes "aged" by cyclic compression in an Instron.
- Feed the measured stiffness and damping into a runner impact model (`code/running_shoe_model.py`).
- *Sustainability angle:* if shoes stay usable longer than the common "replace every 500–800 km" rule of thumb, fewer shoes go to landfill.

**2B. Build the shoe tester itself.** Designing, building and validating a low-cost F1976 tester is a solid project on its own.

**2C. Wearable "shoe health" sensor.** An accelerometer on the shoe tracks how impacts change as the shoe ages. It is novel, but it needs runners (ethics approval and recruitment), so it is riskier.

---

## New, more unique ideas

**U1. "Was the old leather ball more dangerous?"**
- The players in the dementia studies [1, 2] mostly played with leather balls, which soaked up water and got heavier.
- Test a replica vintage leather ball, dry and soaked, against a modern ball on the 1A headform rig. Ball mass affected head response in [5].
- **Twist:** the risk did *not* change between players born in 1910 and 1969 [2]. Your results could help explain why, for example if a wet leather ball turns out less harmful than people assume.
- It is very eye-catching and works best as an **extension of 1A**, because it uses the same rig.

**U2. Football boots on 3G vs grass: a rotational traction tester (ACL injury).**
- Build a portable rig that measures the torque needed to twist a loaded boot on a playing surface.
- Edge-design studs were linked to more ACL injuries [28], and infilled artificial turf gave higher rotational traction than natural grass [29].
- Exeter has both surfaces on campus. This is a strong design-and-build project, but the injury link is indirect.

**U3. Shin guard impact testing.** Drop-test cheap, expensive and children's shin guards on an instrumented "leg", using the BS EN 13061 standard as a guide [30, 31]. It is simple, cheap and very doable, but less novel.

---

## Comparison (1 = poor, 5 = excellent)

| Idea | Engineering content | Novelty | Doable in time | Injury link | Low risk (ethics, kit) | Total /25 |
|---|---|---|---|---|---|---|
| **1A Headform rig + U1 extension** | 5 | 5 | 4 | 5 | 4 | **23** |
| 2A Shoe foam degradation | 5 | 4 | 4 | 3 | 4 | 20 |
| 1B FE model only | 4 | 3 | 4 | 4 | 5 | 20 |
| U2 Traction tester | 5 | 3 | 3 | 4 | 4 | 19 |
| 2B Shoe tester build | 5 | 3 | 4 | 3 | 4 | 19 |
| U3 Shin guards | 4 | 3 | 4 | 3 | 4 | 18 |
| 1C Headgear | 3 | 3 | 4 | 4 | 4 | 18 |
| 2C Shoe sensor | 4 | 4 | 2 | 3 | 2 | 15 |

These scores are my own judgement. Adjust them once your supervisor tells you what equipment is available.

---

## My recommendation

**Project:** *Sport Injury Biomechanics: an instrumented headform study of how ball speed, inflation pressure and neck coupling affect head acceleration in football heading.* The vintage-ball tests (U1) are an extension.

**Why this one:**
- It builds on your own idea.
- It has the strongest injury link and the most engineering: design, build, sensors and modelling.
- It avoids testing on people.
- It gives you a memorable "hook" for the interview.

**Aim:** To quantify how ball speed, inflation pressure and neck coupling change head acceleration in football heading, using a validated low-cost instrumented headform and a mathematical model, in order to inform safer equipment and practice.

**Objectives**
1. Review the literature on heading biomechanics, head-injury measures and ball properties.
2. Develop a mathematical model of ball–head impact and check it against published measurements (already started).
3. Design, build and calibrate a headform–neck rig with a ±200 g accelerometer sampling at 3 kHz or more, and repeatable ball speeds of 5–15 m/s.
4. Measure peak head acceleration, contact time and HIC15 (Head Injury Criterion) for at least 3 pressures × 3 speeds × 2 neck stiffnesses, with at least 5 repeats each.
5. Compare the tests with the model and make evidence-based recommendations, for example on ball pressure for youth football. Extension: wet leather ball vs modern ball.

**What the preliminary model already predicts.** These are testable hypotheses, from `code/heading_impact_model.py`; see `figures/report_fig_heading_model.png`.
- **Speed:** peak head acceleration rises almost in proportion to ball speed, from about 19 g at 9 m/s to about 48 g at 20 m/s (ball at 0.85 atm).
- **Pressure:** going from 1.1 to 0.6 atm (the full Law 2 range [12]) cuts peak head acceleration by **19–24%**. This agrees with the 10–31% that Shewchenko et al. found when halving pressure [5].
- **Neck:** with the head free to move, the model is 20–30% higher than the measured values [4]. It matches them if the neck couples the head to the torso with a stiffness of about **1.2 × 10⁵ N/m**, which suggests players' necks do real work. The rig can test this directly.
- **Sensor:** for balls up to 20 m/s, contact lasts 11–14 ms and peaks stay below about 55 g. A ±200 g sensor sampling at 3.2 kHz (ADXL375 [15]) therefore captures about 35 points per impact.

**Rig concept (discuss with your supervisor)**
- **Head:** a mannequin or 3D-printed head filled to about 4.5 kg, with the accelerometer at its centre of mass. If the department has a Hybrid III headform, use that instead.
- **Neck:** swappable rubber or spring elements of different stiffness, mounted on a heavy "torso" base.
- **Ball delivery:** a ball launcher if Sport and Health Sciences has one. Otherwise use a pendulum, or a drop from height (a 5 m drop gives about 9.5–10 m/s). Measure the real speed with slow-motion video.
- **Electronics:** an ADXL375 accelerometer and an ESP32 or Arduino board logging to an SD card. Use Python to analyse peak g, HIC15 and contact time.

**Backup project:** 2A (shoe foam degradation). Its code is already in this folder too.
