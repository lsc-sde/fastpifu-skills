#!/usr/bin/env python3
"""Generate FastPIFU skills for every specialty in the GIRFT OP Operational Guide (module 2).

Each specialty -> one self-contained, offline skill: SKILL.md (universal PIFU logic +
specialty routing) plus one references/<condition>.md per condition/group, in the same
four-disposition template used by fastpifu-cardiology. Content is drawn faithfully from the
guide; these are first-draft scaffolds for the specialty leads to enrich via the condition
template.
"""
import os, shutil, zipfile, textwrap

OUT = "/home/claude/skills"
SOURCE = ("GIRFT Outpatient Operational Guide, Module 2: Standardising follow-up protocols "
          "(updated June 2026).")

# ---------------------------------------------------------------------------
# SKILL.md universal shell (specialty-agnostic safety logic is fixed text).
# ---------------------------------------------------------------------------
SKILL_TMPL = """---
name: fastpifu-{slug}
description: >
  Assess a {specialty_lc} patient for PIFU (Patient-Initiated Follow-Up) suitability from their
  clinical documents and return a follow-up disposition. Use when deciding what should happen next
  with a {specialty_lc} patient's follow-up — whether they can move to patient-initiated follow-up,
  be discharged, or stay in timed follow-up. Covers {cond_blurb}.
---

<!-- Universal FastPIFU logic (dispositions, safety asymmetry, SOP checklist, output format) lives
in the orchestrator system prompt. This file is {specialty_lc}-specific only. -->

# FastPIFU — {Specialty}

{Specialty} PIFU assessment. Routing, cautions, and hard rules specific to {specialty_lc}; apply
under the FastPIFU orchestrator's universal operating instructions.

## Condition routing

| Condition | Reference file |
|---|---|
{routing}

## Specialty-specific cautions (data-gap traps)

{traps}

## Specialty-specific hard rules

{specialty_rules}
"""

def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "- (none specified in the guide — author per local protocol)"

def render_condition(c):
    out = [f"# {c['name']}", ""]
    out += [f"<!-- concept_ids: (completed by data team) -->",
            f"<!-- author: derived from GIRFT OP guide module 2 | reviewed_by: <lead> | last_updated: 2026-06 -->", ""]
    out += ["## Scope", "", c["scope"], ""]
    out += ["## PIFU — suitable for patient-initiated follow-up", "", bullets(c.get("pifu")), ""]
    out += ["## RETAIN_FOLLOW_UP — timed specialist follow-up still needed", "", bullets(c.get("retain")), ""]
    out += ["## DISCHARGE — no ongoing specialist follow-up needed", "", bullets(c.get("discharge")), ""]
    if c.get("borderline"):
        out += ["## Borderline / uncertain (resolve to RETAIN_FOLLOW_UP, lower confidence)", "", bullets(c["borderline"]), ""]
    if c.get("data"):
        out += ["## Data that must be present to assess", "", "| Required data point | Why it matters |", "|---|---|"]
        out += [f"| {d} | {w} |" for d, w in c["data"]]
        out += [""]
    if c.get("interval"):
        out += ["## Surveillance / review interval", "", c["interval"], ""]
    out += ["## Source", "", c.get("source", SOURCE), ""]
    return "\n".join(out)

def render_skill(spec):
    rows = "\n".join(f"| {c['name']} | `references/{c['file']}.md` |" for c in spec["conditions"])
    traps = "\n".join(f"- {t}" for t in spec.get("traps", [
        "A result or symptom that looks stable in isolation but whose trend is the red flag.",
        "A deferred plan (\"will reassess after X\") which makes PIFU premature.",
    ]))
    rules = "\n".join(f"- {r}" for r in spec["rules"]) if spec.get("rules") else "- None beyond the universal rules."
    return SKILL_TMPL.format(
        slug=spec["slug"], Specialty=spec["Specialty"], specialty_lc=spec["Specialty"].lower(),
        cond_blurb=spec["cond_blurb"], routing=rows, traps=traps, specialty_rules=rules)

def write_specialty(spec):
    base = os.path.join(OUT, f"fastpifu-{spec['slug']}")
    ref = os.path.join(base, "references")
    os.makedirs(ref, exist_ok=True)
    with open(os.path.join(base, "SKILL.md"), "w") as f:
        f.write(render_skill(spec))
    for c in spec["conditions"]:
        with open(os.path.join(ref, f"{c['file']}.md"), "w") as f:
            f.write(render_condition(c))
    # package
    zpath = os.path.join(OUT, f"fastpifu-{spec['slug']}.skill")
    if os.path.exists(zpath):
        os.remove(zpath)
    shutil.make_archive(zpath[:-6], "zip", root_dir=OUT, base_dir=f"fastpifu-{spec['slug']}")
    os.rename(zpath[:-6] + ".zip", zpath)
    return base, len(spec["conditions"])

# ===========================================================================
# DATA  (faithful to the guide; concise first-draft scaffolds)
# ===========================================================================
SPECIALTIES = []

# include the data file
exec(open("/home/claude/skills_data.py").read())

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    total_c = 0
    for spec in SPECIALTIES:
        base, n = write_specialty(spec)
        total_c += n
        print(f"  fastpifu-{spec['slug']}: {n} condition files")
    print(f"\n{len(SPECIALTIES)} skills, {total_c} condition files generated in {OUT}")
