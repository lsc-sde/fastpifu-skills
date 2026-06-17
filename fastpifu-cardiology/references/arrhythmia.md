# Arrhythmia

<!-- concept_ids: (completed by data team) -->
<!-- author: NHS England arrhythmia PIFU guidance + GIRFT module 2 | last_updated: 2026-06 -->

## Scope

Covers atrial fibrillation (paroxysmal, persistent, permanent), atrial flutter,
SVT (AVNRT/AVRT), ventricular tachycardia, ventricular ectopy, pre-excitation
(WPW), and device patients. AF in particular splits sharply between PIFU,
DISCHARGE, and RETAIN depending on subtype and management strategy — read the
relevant subtype block below.

## Universal arrhythmia exclusions (RETAIN_FOLLOW_UP regardless of subtype)

Any one of these excludes PIFU:

- Newly initiated class I or III antiarrhythmic (amiodarone, flecainide, sotalol).
  Identified when: one of these drugs was started recently or is being monitored.
- Device patient (pacemaker, ICD, CRT) without remote monitoring in place.
- Recent cardioversion < 3 months. Identified when: a DCCV date within 3 months.
- Symptomatic arrhythmia with functional limitation (NYHA III–IV equivalent).
- Reversible cause not yet addressed (thyroid disease, electrolyte abnormality).
- High-risk arrhythmia without curative intervention (VT in channelopathy,
  Brugada, complete heart block without a pacemaker).

## Subtype rules

### Paroxysmal AF (PAF)
- PIFU when: recurrent PAF, stable, no class I/III antiarrhythmic, no cardioversion
  < 3 months, stable anticoagulation, no structural heart disease; or patient
  declines/defers ablation but wants ongoing review.
- DISCHARGE when: first episode with a reversible cause now treated; or
  asymptomatic PAF, no structural disease, no ongoing intervention needed; or
  accepted for ablation by EP (EP service takes over).
- RETAIN when: newly diagnosed; class I/III antiarrhythmic just initiated;
  cardioversion < 3 months; symptomatic with functional limitation.

### Persistent AF (> 7 days, cardioversion attempted)
- PIFU when: cardioverted but further treatment deferred (patient choice / other
  pathway) and patient may need reassessment when ready.
- DISCHARGE when: cardioverted and improved with no further referral needed;
  referred to EP (general cardiology discharges); or rate-controlled with good LV
  function, asymptomatic, no rhythm control planned.
- RETAIN when: poor LV function; ongoing antiarrhythmic therapy; recent
  cardioversion; symptomatic; co-existing heart failure.

### Permanent AF (rate-control strategy, HR < 110 bpm)
- DISCHARGE when ALL hold: adequate rate control AND symptom control AND no change
  in heart function AND no other valvular/structural disease needing follow-up.
- RETAIN when: any of those four is not met.

### Atrial flutter (typical / atypical)
- PIFU when: post-successful ablation, symptom-free, no recurrence,
  anticoagulation stable.
- RETAIN when: recurrent flutter on antiarrhythmic; pre-ablation pending;
  persistent flutter on rate control (consider DISCHARGE/GP pathway instead).

### SVT (AVNRT / AVRT)
- PIFU when: post-successful ablation, symptom-free ≥ 3 months, no antiarrhythmic
  needed; or medically managed on stable, well-tolerated medication with
  infrequent episodes.
- RETAIN when: newly initiated medication; frequent breakthrough episodes;
  pre-ablation with EP study pending.

### Ventricular tachycardia (VT)
- PIFU when: VT in a structurally normal heart, successful ablation, asymptomatic,
  preserved LV function, no ICD, medications stable.
- RETAIN when: VT in non-ischaemic cardiomyopathy (inherited cardiomyopathy
  pathway, not PIFU); VT in inherited channelopathy (LQT, Brugada — specialist
  long-term follow-up); ICD in situ without established remote monitoring; recent
  ICD therapy.

### Pre-excitation (WPW pattern)
- PIFU when: asymptomatic on medication, normal LV function, no AF, EP study not
  indicated; or post-ablation and symptom-free.
- RETAIN when: pre-excitation WITH persistent AF (WPW + AF is high-risk, needs
  specialist oversight); pre-ablation with pending EP study; class I antiarrhythmic
  in use.

### Ventricular ectopy
- PIFU when: benign, asymptomatic, no structural heart disease, no antiarrhythmic
  needed.
- RETAIN when: high ectopic burden causing LV dysfunction; symptomatic on
  medication not yet optimised.

### Device patients
- PIFU when: stable pacemaker patient with remote monitoring in place; or ILR
  patient monitored remotely.
- RETAIN when: complex device (CRT-D) with frequent therapies or recent shocks;
  any device without remote monitoring.

## Borderline / uncertain cases (resolve to RETAIN_FOLLOW_UP, lower confidence)

- Pending exercise test or EP study while currently asymptomatic.
- Recent dose increase of rate-control medication.
- Recurrent symptoms (e.g. weekly palpitations) without a documented plan.
- Unplanned admission > 6 months ago without confirmed restabilisation.

## Data that must be present to assess

| Required data point | Why it matters |
|---|---|
| Antiarrhythmic drug class | Class I/III is an exclusion regardless of apparent stability |
| Device + remote monitoring status | No remote monitoring is a hard exclusion |
| Date of last cardioversion | < 3 months is an exclusion |
| Anticoagulation stability | Required for AF/flutter PIFU |
| Structural heart disease / LV function | Distinguishes DISCHARGE from RETAIN |

## Surveillance / review interval

Post-ablation and post-cardioversion PIFU is typically nurse-led, 6–12 months;
GIRFT notes a routine doctor clinic is not required for these. ECG / symptom
review at re-contact.

## Source

NHS England — *Setting up PIFU services for people with arrhythmia*.
GIRFT Outpatient Operational Guide module 2, v1.2 (March 2026).
