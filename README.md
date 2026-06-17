# FastPIFU skill suite

Eleven self-contained, offline FastPIFU skills — one per specialty in the GIRFT Outpatient
Operational Guide (Module 2), plus shared authoring scaffolding.

```
fastpifu-suite/
├── _authoring/          shared templates (skill-template.md, condition-template.md, README.md)
├── fastpifu-cardiology/ (AF, aortic stenosis, heart failure, chest pain, LBBB, POTS, non-pathway)
├── fastpifu-dermatology/
├── fastpifu-ent/
├── fastpifu-gastroenterology/
├── fastpifu-general-surgery/
├── fastpifu-gynaecology/
├── fastpifu-ophthalmology/
├── fastpifu-omfs/
├── fastpifu-orthopaedics/
├── fastpifu-spinal/
└── fastpifu-urology/
```

Each skill: a lean SKILL.md (shared four-disposition PIFU logic + specialty routing) plus one
references/<condition>.md per condition, in the common template. Every skill is offline — all
criteria are bundled; published guidance is cited for provenance only.

The condition files are FIRST-DRAFT scaffolds derived faithfully from the operational guide. They
are intended for the specialty clinical leads to enrich via _authoring/condition-template.md, adding
the concrete "supported when" thresholds the guide does not always specify.

Regenerate the ten guide-derived skills any time from generate_skills.py + skills_data.py.
