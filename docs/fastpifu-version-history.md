**FastPIFU-Cardiology — Version History (v1 → v5)**

*Compiled 2 July 2026 · Focus: exactly what changed in SKILL.md content between each version*

How this document was built

This history is built around actual content diffs between recovered SKILL.md snapshots of each version, read line-by-line and grouped by theme (framing, workflow steps, clinical thresholds, hard rules). Eval accuracy is included only as brief context at the top of each section — the detailed part of every section below is what actually changed in the skill's text and logic.

*Data provenance note: I do not have a tool that can reach your operating system's Recycle Bin from this sandbox. Instead, this session's own scratch space (/tmp) still held leftover build folders and .skill archives from earlier work this session, which happened to contain real SKILL.md snapshots of v1 (via SKILL-backup-2026-06-25.md), v2 (549 lines, timestamped 1 Jul 13:56), v3 (566 lines, 17:34) and v4 (634 lines, 19:19, confirmed byte-for-byte against the v4 eval's own saved context file). v2/v3's snapshot identity is high-confidence (correct chronological order, coherent incremental content) but not cryptographically certain. See the v1 section for one open question about the backup file's identity that I can't resolve from the files available to me.*

At a glance: eval results by version

| Version | Eval date | Accuracy | Per-class (correct/total) | Status |
| --- | --- | --- | --- | --- |
| **v1** | 25 Jun 2026 | **62.0% (93/150)** | ELIGIBLE 34/50 · NOT_ELIGIBLE 47/50 · BORDERLINE 12/50 | Stratified eval |
| **v2** | 1 Jul 2026 | **INVALID (0/150)** | All 150 predictions returned "UNKNOWN" — scoring bug, not a real result | Discarded |
| **v3** | 1 Jul 2026 | **76.67% (115/150)** | ELIGIBLE 41/50 · NOT_ELIGIBLE 49/50 · BORDERLINE 25/50 | Best-performing iteration |
| **v4** | 1 Jul 2026 | **73.33% (110/150)** | ELIGIBLE 45/50 · NOT_ELIGIBLE 46/50 · BORDERLINE 19/50 | Regression from v3 |
| **v5** | 2 July 2026 | **84.0% (126/150)** | ELIGIBLE 45/50 • NOT_ELIGIBLE 50/50 • BORDERLINE 31/50 | Best score of any version; see full results section below |

**v1 → v2 : Spec-compliance cleanup pass**

*v1 scored 62.0% (25 Jun eval); v2's own eval run failed technically (see summary table) so v2's real accuracy was never measured. This transition reads as a restructuring/compliance pass, not a clinical-content rewrite — most changes are condensation and renaming, with a few substantive drops and one major hard-rule reversal.*

Structure and framing

  - Step headers renamed for Anthropic-spec conventions: "STEP 1 — Gain Background Knowledge" → "STEP 1 — Load NHS Reference Files"; "STEP 4 — Final Output" → "STEP 4 — Structured Output."

  - Overview rewritten around a single guiding question ("what should happen next with this patient's specialist follow-up?") instead of a longer multi-paragraph preamble; the ELIGIBLE / BORDERLINE / NOT_ELIGIBLE three-way definitions were formalised into an explicit bullet block for the first time — this exact block persisted through every later version with only wording tweaks.

  - "Non-pathway conditions" collapsed from a 4-item bulleted list (POTS; stable angina/IHD/post-MI; cardiomyopathies DCM/low-risk HCM; other) into a single inline sentence naming the same conditions.

  - The entire POTS factors-for/factors-against list (~25 lines, inline in v1) was extracted into a new file, references/pots-guidance.md, replaced in SKILL.md with a short pointer — the first instance of the "move detail to a reference file, leave a stub" pattern that v5 later applied to Step 2d.

  - A pointer sentence to a new references/condition-rules.md was added ahead of Step 2d, though the full inline rule tables (discharge scenarios, HF, arrhythmia, valve disease) were still kept in SKILL.md itself — the stub pattern wasn't actually completed for Step 2d until the v5 rebuild this session.

  - The standalone "What PIFU is (plain language)" explainer section (~14 lines, aimed at human readers rather than decision logic) was dropped entirely from Reasoning Transparency.

Clinical content: mostly condensation, two substantive drops

  - SVT: dropped "EP study pending" from the Not-for-PIFU list.

  - Ventricular ectopy: dropped the explicit note that beta-blockers used for symptom control don't count as antiarrhythmics requiring monitoring (partially reinstated in v3/v4).

  - Aortic regurgitation: dropped the explicit statement that asymptomatic, haemodynamically stable moderate AR with documented LV surveillance meets PIFU criteria, and dropped its dedicated borderline band (LVESD 45–50mm; EF 50–55%).

  - All other subtype rules (HF, PAF/permanent/persistent AF, VT, pre-excitation, atrial flutter, AS, MR, MVP, BAV, post-intervention) carried through with wording tightened but no criteria changed.

Hard Rules — the most consequential single change in this transition

*v1's Hard Rules literally said: "If uncertain between BORDERLINE and NOT_ELIGIBLE, err toward NOT_ELIGIBLE — a false negative (missed PIFU candidate) is safer than a false positive (unsafe patient on PIFU)." v2 reversed this outright, replacing it with: "prefer BORDERLINE — it prompts clinician review rather than defaulting to unnecessary timed follow-up," and added a new companion rule: "Do not call BORDERLINE when no exclusion flags are present — do not manufacture uncertainty." This "prefer BORDERLINE when uncertain" principle, first introduced here, is the direct ancestor of v5's much more explicit hard rule — yet the BORDERLINE→NOT_ELIGIBLE misclassification pattern persisted through v3 and v4 regardless, which is why v5 escalated from general guidance to six explicitly named scenarios.*

**v2 → v3 : Restoring detail, few net-new additions**

*v3 scored 76.67% — the best of any measured iteration. This was a much smaller, surgical transition: mostly restoring specific detail that v2's condensation pass had accidentally dropped, plus a handful of genuinely new additions.*

Restored detail (lost in v1→v2, added back)

  - Discharge-to-GP table: restored explicit "discharged to GP" wording on the BAV row, and restored dedicated rows for aortic-stenosis surveillance and general heart-failure discharge that v2 had merged away.

  - PAF: restored the explicit reversible-cause examples (hyperthyroidism, sepsis, GA, thoracic surgery) and the electrophysiology-referral branching detail that v2 had condensed to one line each.

  - Persistent AF: restored the explicit >7-day/cardioversion-attempt definition and the "cardioverted but treatment deferred → PIFU" branch; restored "recent cardioversion" to the Not-for-PIFU list.

New additions

  - Arrhythmia careful-consideration list: added "complex comorbidities with uncertain interaction requiring coordinated specialist review."

  - Aortic stenosis: added a second progression tier — ">0.6 m/s/year is a hard concern" on top of the existing ">0.3 m/s/year is a surveillance warning."

  - Data gaps table: added a new row, "Syncopal frequency — ≥1/month = POTS exclusion."

  - Common traps: added "Patient is functionally NYHA II but has documented non-compliance with self-monitoring or diuretic non-compliance — not suitable for PIFU."

  - Hard Rules: added a worked example to the optimisation rule — "(e.g. bradycardia limiting beta-blocker uptitration)."

*Net effect: v3 was essentially v2's tighter structure with v1's clinical detail restored more precisely, plus a few small genuinely new additions — no large rewrites. This combination produced the best score of any version.*

**v3 → v4 : Largest single expansion, but a regression**

*v4 scored 73.33%, down 3.3 points from v3 — despite this being the largest content expansion of any transition (566 → 634 lines), much of it aimed directly at reducing false NOT_ELIGIBLE calls.*

Absolute exclusions

  - Added a major carve-out distinguishing a genuine "outstanding investigation" from routine surveillance imaging — explicitly stating that a scheduled echo or characterisation MRI for known stable AR/BAV does NOT count as a pending investigation and is a BORDERLINE trigger, not a hard exclusion.

Heart failure — softened admission rule

  - Replaced the flat "no admission within 6 months" hard exclusion with "clinical stability established — a recent admission does not automatically disqualify if demonstrably restabilised," and rewrote Not-for-PIFU to require multiple unplanned admissions (a pattern of instability) rather than any single one.

  - Split GDMT optimisation guidance by HF subtype: HFrEF requires all four drug classes; HFmrEF explicitly states that absent SGLT2i alone must NOT downgrade an otherwise-ELIGIBLE case (flag as a data gap only).

  - Expanded Borderline list with "single recent unplanned admission (including if the letter IS the discharge summary) where the patient is now improving."

Arrhythmia — NHS-verbatim quoting introduced

  - SVT: added a direct NHS-source quote ("managed successfully with medication: consider LONG-TERM PIFU") and a new Borderline tier for ablation being discussed but not yet committed.

  - Pre-excitation (WPW): added an NHS-verbatim quote and tightened the rule to require an explicit specialist/MDT risk-stratification decision (not just "no AF") before PIFU is appropriate, with a new Borderline tier for WPW+AF assessed by MDT but not explicitly endorsed for PIFU.

  - Atrial flutter: added an NHS-verbatim quote distinguishing atypical flutter/AT (long-term PIFU candidate) from typical flutter with imminent ablation (not for PIFU), plus a new Borderline tier.

Valve disease — entry-criteria corrections

  - Mitral regurgitation: added an NHS-source clarification that "LVEF <60%" is a PIFU-exit/monitoring trigger, not an entry criterion, resetting the practical entry threshold to LVEF ≥ 55% with a new Borderline band at 55–59%.

  - Mitral valve prolapse: mirrored the same LVEF ≥ 55% entry logic with its own borderline carve-out requiring explicit clinician endorsement.

  - Post-valve intervention: major rewrite — added an NHS-verbatim quote establishing TAVI/TEER/bioprosthetic/repair as explicitly PIFU-suitable with NO timing restriction, with the real gating criterion being whether a post-operative TTE was performed (not time elapsed since procedure). This removed an implicit "<3 months = exclusion" rule that had existed since v1.

Hard Rules — formalised the "strong flag → BORDERLINE" framework

  - Replaced the flat "recent hospitalisation <6 months (HF) / <3 months (arrhythmia) = do not recommend PIFU" rule with an explicit framework: strong exclusion flags typically preclude PIFU but indicate BORDERLINE (not NOT_ELIGIBLE) when a clearly positive trajectory is present; NOT_ELIGIBLE reserved for flags that are unambiguous and unmitigated.

*Despite all of this — more NHS-verbatim grounding and repeated attempts to redirect single/isolated exclusion flags toward BORDERLINE — BORDERLINE recall fell to its lowest point of any version (38%), and 31 of the 40 total errors were still BORDERLINE cases misclassified as NOT_ELIGIBLE. The added length and density of numeric caveats appears to have diluted the core signal rather than reinforcing it. Separately, this session's NHS-verbatim re-verification found several numeric thresholds that had been present since v1 or introduced in v3/v4 do not actually appear in the NHS source documents — the AS Vmax <4.0 m/s entry cutoff (a general-cardiology severe-AS threshold, not NHS PIFU-specific), a fabricated >45mm BAV aortic-root cutoff, and unsourced LVESD/EROA borderline bands for MR.*

**v4 → v5 : This session's rebuild**

*v4 scored 73.33%; v5 scored 84.0% (126/150), the best of any version — see the "v5 Evaluation Results" section below for the full breakdown. This transition directly targeted the one failure mode present in every measured version: BORDERLINE cases defaulting to NOT_ELIGIBLE.*

Structural

  - Finally completed the "move detail out of SKILL.md, leave a stub" pattern that v2 had started for Step 2d but never finished: collapsed the ~270-line inline Step 2d subtype block (which had kept growing inline through v1–v4) down to a short pointer to references/condition-rules.md.

The core fix: closing the BORDERLINE→NOT_ELIGIBLE gap

  - Added six explicitly named "always BORDERLINE, never NOT_ELIGIBLE" scenarios: age not stated, stability undocumented, follow-up plan deferred, medication optimisation unclear, severity/LV status unclear, symptoms resolved on a recently-initiated drug.

  - Added a hard rule: data gaps produce BORDERLINE, not NOT_ELIGIBLE — the most explicit, named version yet of a principle that has been drifting through every version since v2's initial "prefer BORDERLINE" reversal without ever fully closing the gap in practice.

Numeric threshold corrections (NHS-verbatim re-verification)

  - Aortic stenosis: corrected entry threshold from <4.0 m/s (used unchanged since v1 — actually the general-cardiology severe-AS definition) to the NHS-sourced <3.5 m/s.

  - Bicuspid aortic valve: corrected from the fabricated >45mm aortic-root cutoff (present since v1) to the NHS-sourced 40mm imaging-interval trigger.

  - Mitral stenosis: added the NHS-sourced MVA >1.5cm² entry criterion — a condition with no explicit entry rule in any prior version.

  - Heart failure: added a source-fidelity note explicitly labelling several long-standing numeric thresholds (eGFR bands, K+, titration windows) as supplementary clinical judgement rather than NHS-sourced — the first time this distinction was made explicit anywhere in the version history.

Condition classification

  - Reclassified chest pain / stable angina / post-MI out of the general non-pathway bucket (where it had sat since v1, tested against the elevated six-criteria bar) into its own GIRFT-informed tier with dedicated Step 2d rules.

  - Moved cardiomyopathy / inherited channelopathy out of the general non-pathway bucket (also there since v1) into the NHS-pathway bucket via the arrhythmia source.

Restorations and packaging

  - Restored the WPW+AF high-risk-by-default safety nuance (present in v1, progressively softened through v2–v4) and an atrial-flutter borderline trigger that had been dropped.

  - Repackaged with a verified flat zip structure, re-audited against all 23 Anthropic skills-spec checklist items, and redrew the architecture diagram to match the current three-tier condition logic.

**Post-compilation fixes (2 July 2026, after this document was first built)**

*Three further fixes were made during a subsequent no-shortcuts NHS-verbatim re-verification pass, after this document was originally compiled. Listed here so this history stays accurate.*

  - Fixed a stale Step 2b header that still read 'non-pathway conditions (POTS, angina, post-MI, etc.)', contradicting the Overview's GIRFT-informed reclassification of chest pain/angina/post-MI — found by re-grepping every angina/post-MI/cardiomyopathy mention in SKILL.md.

  - Fixed four gaps found by re-fetching all five live NHS/GIRFT pages and checking condition-rules.md line-by-line: missing ventricular-ectopy-specific NHS timescales (1-year and 2-year re-checks, calcium-channel-blocker inclusion), a missing 'other arrhythmias' catch-all category, missing valve-disease imaging intervals for AR/MR/MS/post-intervention, and a missing distinct mechanical-valve-prosthesis pathway (no imaging follow-up required at all, unlike bioprosthetic/TAVI).

  - Added an NHS-sourced exclusion clarification to Step 2a: 'unable to take responsibility for self-initiated care' includes rapidly progressing dementia, severe memory loss, and severe learning disability — mitigated only if a carer or care-home/GP administrative support is explicitly documented.

**Deep-verification sweep (2 July 2026, 14:48 rebuild)**

*A further comprehensive sweep of every reference document, cross-checked against live NHS/GIRFT sources and against each other, found and fixed six more issues. Listed here so this history stays accurate.*

  - Fixed the nhs-pifu-what-is-pifu reference file itself (not just SKILL.md): it was missing the live source's dementia/severe-memory-loss/severe-learning-disability example and the care-home/GP-surgery administrative booking-support nuance, even though SKILL.md's own operative text already had the dementia/carer clarification from the previous round — the underlying 'source of truth' reference file was incomplete.

  - Added NHS-sourced-vs-supplementary sourcing disclosure to the Universal Arrhythmia and Universal Valve Exclusions lists in condition-rules.md and nhs-pifu-criteria-summary.md, after full-text search of both source documents found: the valve document does contain a genuine verbatim universal 'NOT Suitable' list (now cited precisely), but the arrhythmia document has no equivalent list at all, and two of its four 'universal' bullets (reversible-cause/thyroid/electrolyte; high-risk-arrhythmia/complete-heart-block) do not appear anywhere in that source and were unlabelled synthesis.

  - Added a previously-missing NHS-verbatim discharge scenario to the Discharge-to-GP table: valve disease patients whom the clinician has deemed unsuitable for valvular intervention due to frailty or multiple co-morbidities, with no surveillance plan documented, map to Discharge — this exact scenario was quoted in the new sourcing-disclosure note but had never been operationalised as an actual rule.

  - Deliberately did NOT harden three other NHS-listed valve exclusions (complex HVD needing regular review, low health literacy, difficulty contacting the service) into automatic NOT_ELIGIBLE, despite the source listing them under its universal 'NOT Suitable' banner — Step 2a already treats these as BORDERLINE-capable 'careful consideration' factors, and hardening them would reintroduce the v4 regression pattern this rebuild exists to fix. Disclosed explicitly as an intentional policy choice, not a silent gap.

  - Corrected PIFU-links.txt, which still cited the GIRFT v1.2 March 2026 URL, to cite the same v1.3 June 2026 URL that the GIRFT reference file's own 'Original source' field records (the v1.2 URL redirects to v1.3; cardiology content confirmed unchanged between versions).

  - Corrected a stale '...none exists for POTS as of June 2026' date in pots-guidance.md to 2 July 2026, and corrected two stale claims in this project's own compliance checklist (item 7 said SKILL.md was 400 lines; it is 441. Item 20 said the extraction-date note read '25 June 2026'; it reads '2 July 2026').

**Sweep continued — a self-correction and one more genuine gap (2 July 2026, 14:54 rebuild)**

*Continuing the same sweep, a full line-by-line re-read of the arrhythmia and valve source documents (rather than targeted greps) found that one of this sweep's own earlier disclosure notes was itself wrong, plus one further genuine gap. Listed here in the interest of the same rigor being applied to this document's own claims.*

  - Self-correction: this sweep's own earlier note claimed 'the NHS arrhythmia document contains no single universal-exclusions section.' A full re-read found this was wrong — the source has a verbatim 'General Inclusion and Exclusion Criteria' section at the top (outstanding investigations/decisions; cannot easily contact the service; low knowledge/skills/confidence and/or no carer support). Also found on this re-read: the 'device without remote monitoring' bullet was NOT actually traceable to the CRM Devices section as previously claimed — that section only mentions remote monitoring as a review tool, not a PIFU precondition. Both corrected in condition-rules.md and nhs-pifu-criteria-summary.md, alongside the same disclosed-policy-choice treatment already applied to valve disease and heart failure.

  - Added a previously entirely-missing NHS-verbatim BAV exclusion, found on a full read of the valve source: 'If echocardiogram cannot assess aortopathy alone, patient is NOT suitable for PIFU' — distinct from the aortic-root-size triggers, this is about imaging adequacy itself, not root dilatation.

  - Added the same disclosed-policy-choice treatment to heart failure that valve disease already had: the NHS HF source's 'Patients NOT Suitable for PIFU' list also names inability to contact the service and low knowledge/skills/confidence/no carer support as hard exclusions, which Step 2a deliberately treats as BORDERLINE-capable instead.

  - Cross-checked the generic PIFU SOP template against SKILL.md Step 2a and found independent triple-confirmation of the dementia/carer fix: the SOP template's own 'Identifying patients for whom PIFU is suitable' section states the same dementia/severe-memory-loss/severe-learning-disability example and care-home/GP-surgery booking-support nuance, verbatim, matching what was added to SKILL.md and the what-is-pifu reference file earlier this session.

**Fourth sweep — full re-reads of every file, one diagram fix (2 July 2026)**

*Per Karthik's request for a sweep that finds zero errors before authorising eval data, this pass did a complete top-to-bottom re-read of every file (not grep-based spot checks): the full ~500 remaining lines of the SOP template, SKILL.md fresh end-to-end, condition-rules.md fresh end-to-end, nhs-pifu-criteria-summary.md fresh end-to-end, the architecture SVG's full text content, and this document plus the compliance checklist for internal coherence.*

  - The SOP template's remaining ~500 lines (roles/responsibilities, monitoring, booking processes) are confirmed purely administrative — no clinical eligibility content was missed there.

  - SKILL.md, condition-rules.md, and nhs-pifu-criteria-summary.md all read internally consistent on a fresh full pass — no contradictions, no duplicate headers, no stale cross-references found.

  - One genuine staleness found: the architecture SVG's 'Conditions Covered' box listed the arrhythmia subtypes but omitted 'Other Arrhythmias' (inappropriate sinus tachycardia / low-burden SVE) — a named subtype section added to condition-rules.md earlier this session but never reflected back into the diagram. Fixed and re-rendered to confirm no text overflow. Note: the SVG is a supporting document, not packaged inside the .skill file itself, so this did not require a package rebuild.

**v5 Evaluation Results (2 July 2026)**

*Production-equivalent run: 150 fresh cases (evals/eval_sample_150_v3.json, 50 ELIGIBLE + 50 NOT_ELIGIBLE + 50 BORDERLINE, zero overlap with v1–v4 eval sets), 15 subagents × 10 cases each, each subagent given only the clinic letter text (ground truth withheld) plus the full skill context. Scored externally against the hidden _class labels afterward.*

Overall accuracy: 84.0% (126/150), the best of any scored version, up from v4's 73.3% and v3's 76.7%. Per-class accuracy: ELIGIBLE 90.0% (45/50), NOT_ELIGIBLE 100% (50/50), BORDERLINE 62.0% (31/50).

Error breakdown (24 total errors)

  - True BORDERLINE → predicted NOT_ELIGIBLE: 19 cases — the same failure mode that has dominated every prior version, though reduced from 31/40 errors in v4 to 19/24 here.

  - True ELIGIBLE → predicted NOT_ELIGIBLE: 3 cases.

  - True ELIGIBLE → predicted BORDERLINE: 2 cases.

  - True NOT_ELIGIBLE → predicted anything else: 0 cases — NOT_ELIGIBLE precision and recall were both perfect on this set.

Root cause 1: the six "always BORDERLINE" scenarios are still being reasoned past

Broken down by the eval's own scenario tags, the 19 BORDERLINE→NOT_ELIGIBLE errors split as: clinical stability unclear (7), follow-up plan unclear (4), condition severity/LV status unclear (3), age not stated (3), medication optimisation unclear (2). These are exactly the six scenarios v5 named explicitly as always-BORDERLINE. Reading the actual letters (e.g. idx 262, 825, 442) shows the pattern is not genuine ambiguity a human would struggle with — the clinician has openly deferred a decision ("further risk stratification is required," "an echocardiogram is pending to reassess," age genuinely not documented), and the model is treating that deferral as a positive exclusion finding rather than the absence of one. The rule exists in prose but is not functioning as a hard gate the model must satisfy before concluding NOT_ELIGIBLE.

Root cause 2: two new, smaller failure types

  - Pre-excitation over-exclusion (idx 3296, 3722): both are incidental WPW/pre-excitation found alongside a different, well-managed arrhythmia, where the MDT explicitly declined EPS with a documented clinical rationale (stable pattern, asymptomatic pathway, patient preference) and then placed the patient on PIFU. The model applied a blanket "no EPS → NOT_ELIGIBLE" rule without allowing for a reasoned, documented clinician decision to skip EPS on a low-risk incidental pathway.

  - "Discharge" terminology conflation (idx 3115): a persistent-AF letter titled "Discharge Summary" is actually discharging the patient from routine clinic appointments onto a PIFU pathway, not discharging them to GP with no further specialist input. The model pattern-matched on the word "discharge" rather than reading what the patient is being discharged to.

  - Over-caution on clearly-ELIGIBLE cases (idx 4887, 3883): stable moderate AR and stable HFmrEF with a short, fully-resolved admission, both explicitly recommended for PIFU by the clinician, were marked down to BORDERLINE — the opposite failure direction, suggesting the recent-admission caution heuristic can fire even when the letter itself concludes with an explicit, well-supported PIFU recommendation.

Areas identified for the next iteration

  - Convert the six "always BORDERLINE" scenarios into an explicit pre-verdict checklist — e.g. "before concluding NOT_ELIGIBLE, confirm the exclusion is a stated positive fact, not an absence of information" — rather than prose the model can reason past.

  - Add explicit guidance that a documented MDT/clinician rationale for skipping EPS on an incidental, asymptomatic accessory pathway is evidence that risk stratification occurred, not evidence that it didn't.

  - Clarify DISCHARGE vs PIFU disambiguation: the word "discharge" in a letter title or phrase is not dispositive — what matters is whether the patient is discharged to GP with no further cardiology role (DISCHARGE/NOT_ELIGIBLE) or discharged from routine clinic appointments onto a PIFU pathway (ELIGIBLE).

  - Check whether the recent-admission downgrade heuristic is firing too readily on discharge summaries that themselves conclude with an explicit, well-supported PIFU recommendation.

Cross-version pattern

One failure mode is present in every version that was actually scored: BORDERLINE cases being misclassified as NOT_ELIGIBLE — 36 of 57 errors in v1, 22 of 35 in v3, 31 of 40 in v4, and 19 of 24 in v5. What's notable from the content diffs is that the underlying principle ("prefer BORDERLINE when genuinely uncertain") was already stated in v2, restated in v3, and given an entire explicit framework in v4 — and the error pattern got worse, not better, across that span. v5's hard rule with six named scenarios measurably reduced this failure mode: total errors fell from 40 to 24 and BORDERLINE recall rose from 38% to 62%, so this specific gap genuinely narrowed — but it is still the largest single error category, which suggests the rule is functioning as prose guidance the model can reason past on a given letter rather than a gate it is forced to satisfy before concluding NOT_ELIGIBLE. See the v5 Evaluation Results section above for the detailed breakdown and the likely next step.

**Post-v5 update (this session): external verdict vocabulary added**

To align with the lsc-sde/fastpifu-skills repo's shared FastPIFU orchestrator vocabulary, SKILL.md now adds a translation layer at Step 4 (Structured Output): internal classifications (ELIGIBLE/NOT_ELIGIBLE/BORDERLINE/DISCHARGE — unchanged, still what the eval harness scores) map to external verdict words PIFU/RETAIN_FOLLOW_UP/DISCHARGE/INSUFFICIENT_DATA, with BORDERLINE cases ≥70% confidence rendered as `RETAIN_FOLLOW_UP — BORDERLINE` (never a bare, indistinguishable RETAIN_FOLLOW_UP) and BORDERLINE cases <70% confidence rendered as `INSUFFICIENT_DATA`. All six reference documents converted from .docx to .md, with SKILL.md's Step 1/Step 2 Read paths updated accordingly, since the target repo's skill format is markdown-only.
