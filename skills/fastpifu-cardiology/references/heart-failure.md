# Heart Failure (HFrEF / HFmrEF / HFpEF)

<!-- concept_ids: (completed by data team) -->
<!-- author: NHS England HF PIFU guidance + GIRFT module 2 | last_updated: 2026-06 -->

## Scope

Covers chronic heart failure across all phenotypes: reduced ejection fraction
(HFrEF), mildly-reduced (HFmrEF), and preserved (HFpEF). The single strongest
exclusion across all phenotypes is a recent unplanned admission — it disqualifies
even patients who look well in clinic.

## PIFU — suitable for patient-initiated follow-up

All of the following must hold:

- Criterion: Clinically stable, NYHA Class I–II.
  Supported when: NYHA class is explicitly documented as I or II and there is no
  description of acute decompensation.
- Criterion: No unplanned hospital admission in the past 6 months.
  Supported when: the letter states no admissions, or the last admission date is
  > 6 months ago.
- Criterion: Guideline-directed medical therapy (GDMT) is optimised.
  Supported when, for HFrEF/HFmrEF: all four drug classes present (ACEI/ARB/ARNI,
  beta-blocker, MRA, SGLT2i) at or approaching target doses. For HFpEF: diuretic
  optimised and SGLT2i started if indicated. Low/sub-therapeutic doses with no
  documented uptitration plan are NOT "optimised".
- Criterion: No active titration or recently initiated agent.
  Supported when: no medication started or changed within the last 8–12 weeks.
- Criterion: Stable renal function.
  Supported when: eGFR trend is flat or improving (watch for post-ARNI drops).
- Criterion: No electrolyte instability.
  Supported when: K+ within range and not rising (hyperkalaemia on MRA/ARNI is a
  common trap).
- Criterion: Evidence of patient self-monitoring.
  Supported when: a weight diary, fluid-balance awareness, or traffic-light
  symptom plan is documented.

## RETAIN_FOLLOW_UP — timed specialist follow-up still needed

Any one of these excludes PIFU:

- Feature: NYHA Class III–IV. Identified when: NYHA documented as III or IV, even
  if partially treated.
- Feature: Recent unplanned admission < 6 months. Identified when: an admission
  date within 6 months appears anywhere — a hard exclusion regardless of current
  appearance.
- Feature: Awaiting device therapy. Identified when: CRT/ICD or resynchronisation
  is planned or referred.
- Feature: Medication not yet optimised or being uptitrated. Identified when: a
  titration plan is in progress or doses are sub-target without a documented
  ceiling reason.
- Feature: Renal decline. Identified when: eGFR < 30, or actively declining after
  a recent medication change.
- Feature: Significant electrolyte abnormality. Identified when: K+ > 5.5 or rising.
- Feature: Complex comorbidity interaction requiring coordinated specialist review.

## DISCHARGE — no ongoing specialist follow-up needed

- Scenario: HFpEF fully investigated, hospital clinic input no longer required,
  community HF team managing. Identified when: the letter hands ongoing care to
  the community HF team / GP with no specialist review planned.
- Scenario: Episode concluded with explicit discharge wording. Identified when:
  "no further specialist input needed" or equivalent.

(HFpEF rarely needs a hospital clinic appointment once optimised — GIRFT.)

## Borderline / uncertain cases (resolve to RETAIN_FOLLOW_UP, lower confidence)

- Recent medication change (< 12 weeks) but otherwise stable — reassess after
  titration completes.
- LVEF in the 40–50% range without a documented stability trajectory.
- Last admission > 6 months ago but restabilisation not explicitly confirmed.
- Diuretic use unclear (PRN vs regular) — not "optimised" without a fixed regimen.
- Three or more comorbidities with uncertain interaction.

## Data that must be present to assess

| Required data point | Why it matters |
|---|---|
| NYHA class | Sets the eligibility threshold; missing → flag as gap |
| LVEF (quantified %) | Borderline 40–50% range changes the picture |
| Date of last hospital admission | < 6 months is a hard exclusion |
| eGFR trend | Post-ARNI drop can exclude an otherwise stable patient |
| Electrolytes (K+) | Hyperkalaemia on MRA/ARNI is a common trap |

## Surveillance / review interval

PIFU period typically 12 months. Optimisation should be performed by the
community HF team where an SLA exists.

## Source

NHS England — *Setting up PIFU services for people with heart failure*.
GIRFT Outpatient Operational Guide module 2, v1.2 (March 2026), Cardiology — Heart Failure.
