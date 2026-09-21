# ODD Feature: Complementary AI Traceability Annex

## Objective

Create one Spanish complementary evidence annex that explains the team's Gentle AI + Engram Cloud workflow and presents the substantive prompts filtered from a raw universe of 343 prompts, without replacing the mandatory section-oriented declaration form.

## Problem

The current version 1.0 is mainly a future-facing traceability template. It does not adequately explain why a complementary annex is necessary, how the whole team used the Gentle AI ecosystem with Engram Cloud, or what the existing prompt/session/observation corpus actually contains. The submission needs evidence, not primarily empty fields.

## Why

The mandatory form is organized by final-report section and cannot readably carry the team's entire cross-member AI trail. Engram Cloud provided shared persistent context across local team workflows: prompts, observations, sessions, and recorded decisions could be consulted by other authorized team members and agents. The complementary annex must explain that collaborative value and present the substantive prompt evidence after a transparent relevance filter. The raw total of 343 prompts is an input to audit, not a claim that all 343 belong in the final catalog.

## Scope

### In scope

- Maintain one complementary annex in professional Spanish at the repository root.
- Explain why the mandatory section-oriented form needs this complementary evidence document.
- Explain the team's verified Gentle AI + Engram Cloud collaboration model and its communication value.
- Audit the raw universe of 343 prompts using explicit relevance criteria.
- Embed the complete filtered substantive prompt catalog in the same annex.
- Connect prompts with sessions, observations/decisions, FP/Jira, artifacts, GitHub history, and human review when evidence exists.
- Preserve explicit safeguards for sections that require exclusive human authorship.

### Out of scope

- Replacing or completing the mandatory declaration form.
- Inventing contributor names, prompt IDs, Jira links, Engram session IDs, commits, reviews, or validation outcomes.
- Creating a second catalog annex or a third supporting annex.
- Mutating Jira, GitHub, or Engram Cloud.
- Publishing credentials, private data, or unrelated project prompts.
- Claiming that aggregate metrics or platform presence prove full traceability.

## Constraints

- Governing source: `INVESTIGACION/Indicaciones Trabajo de Investigacion 2026.pdf`, especially sections 6.1–6.4.
- Existing mandatory form: `Anexo Declaración de Uso de IA - ONEBYTE - TI-06.md`.
- The new annex must explicitly state that it supplements and does not replace the mandatory form.
- Missing evidence must be labeled as pending or unavailable; it must never be inferred.
- Existing unrelated modification `docs/onboarding-engram-cloud-windows.md` must not be changed.
- No commit will be created because the user did not explicitly request one.

## Delivery and routing

- Delivery strategy: `exception-ok` for this document-only work; the user explicitly requires one evidence document instead of additional annexes.
- Revised forecast: likely above 400 authored lines because the single annex must embed the complete filtered catalog; keep one document because splitting it would violate the confirmed submission format.
- TDD mode: not applicable to this documentation-only work; verification is structural and content-based.
- Task T1 route: delegated direct writer.
- Trigger evidence: repository preparation spans more than four evidence files and the annex is a non-mechanical documentation artifact.
- Planned output: `Anexo Complementario de Trazabilidad de Uso de IA - ONEBYTE - TI-06.md`.

## Tasks

- [x] **T1 — Draft the complementary annex**
  - Describe the traceability model and the distinct evidentiary role of Jira, GitHub, and Engram Cloud.
  - Include the reported aggregate metrics only as contextual inventory, clearly labeled as pending snapshot verification.
  - Add a section-level coverage table aligned with the mandatory declaration form.
  - Add the canonical detailed-record schema:
    `ID | Sección final | Nivel | Integrante responsable | FP/Jira | Fecha | Herramienta + versión + modelo | Prompt efectivo | Sesión/exportación Engram | Artefacto y versión | Commit SHA | PR/Issue | Revisión técnica | Validación humana | Estado | Observaciones/límites`.
  - Include at least one explicitly illustrative example that cannot be mistaken for completed evidence.
  - Include evidence-state definitions and a bidirectional completeness procedure.
  - Safeguard human-only sections and individual declarations.
  - **Acceptance:** one self-contained Spanish Markdown annex exists at the planned output path, contains no fabricated evidence, and distinguishes aggregate inventory from traceable records.
  - **Checks:** heading/section inspection; search for required terms; review all factual examples against existing repository evidence.

- [x] **T2 — Verify and reconcile**
  - Read back the annex and compare it against sections 6.1–6.4 and the existing mandatory form.
  - Confirm no unrelated files changed.
  - Confirm the annex does not imply that Jira, Git, or Engram alone establishes human authorship or full compliance.
  - **Acceptance:** verification evidence is recorded below and any gap is left open rather than silently accepted.
  - **Checks:** focused diff, Markdown structure, required-field review, and prohibited-claim review.

- [x] **T3 — Audit and classify the 343-prompt source corpus**
  - Locate the Engram Cloud/project source that supports the user-reported universe of 343 prompts.
  - Define and apply explicit relevance categories: substantive, operational, vague, duplicate, and unrelated.
  - Preserve a reproducible count of included and excluded prompts, with exclusion reasons.
  - Map substantive prompts to sessions, observations/decisions, responsible member when available, FP/Jira, and generated artifacts.
  - **Acceptance:** the prompt universe and filtering method are reproducible; missing fields remain explicit.
  - **Checks:** source count, category totals, duplicate handling, and representative record review.

- [x] **T4 — Rewrite the annex as a single evidence document**
  - Replace the template-first framing with the actual reason for the complementary annex: the mandatory form is section-oriented, while the team's Gentle AI and Engram Cloud workflow generated a large cross-member evidence corpus that requires a readable consolidated record.
  - Explain how shared Engram Cloud sessions, observations, prompts, and recorded decisions improved communication between local agents and team members without overstating real-time capabilities beyond verified evidence.
  - Include the complete filtered substantive prompt catalog in this same document, not in an additional annex.
  - Include filtering results, session/observation context, decision traceability, and links to Jira/GitHub evidence where available.
  - Retain only concise methodology and safeguards that directly help interpret the evidence.
  - **Acceptance:** one document explains why it exists and presents the filtered evidence itself rather than primarily offering empty templates.
  - **Checks:** purpose clarity, complete filtered catalog, count reconciliation, source traceability, and no fabricated metadata.

- [x] **T5 — Verify the rewritten evidence annex**
  - Confirm the raw prompt total, included/excluded totals, criteria, mappings, and claims against the available source.
  - Confirm the document remains complementary to the required course form and protects human-only sections.
  - Confirm no additional annex file was created.
  - **Acceptance:** independent verification passes or remaining source limitations are reported as blockers.
  - **Checks:** structural readback, source-to-document samples, count arithmetic, diff check, and repository status.

## Progress

- Repository mapping completed by a read-only exploration worker.
- Evidence found in `docs/research-log/*.md`, `odd/tasks/fp187-flujo-caja-van-tir.md`, `odd/tasks/fp188-recomendacion-tecnica-economica.md`, Git history, Engram configuration/guides, and the mandatory declaration form.
- Main observed gap: no complete section-to-person-to-prompt-to-artifact-to-version-to-validation matrix.
- T1 completed by the delegated writer: `Anexo Complementario de Trazabilidad de Uso de IA - ONEBYTE - TI-06.md` was created.
- Writer checks passed: non-empty file, required-term search, `git diff --check`, and repository status inspection.
- Known open evidence gaps remain intentionally visible: dated Engram inventory export, stable Engram references, individual ownership, and completed human validations.
- T2 completed: independent verifier returned PASS with no blocking findings.
- Parent spot check confirmed the annex wording against the previously extracted text of PDF sections 6.1–6.4 and reran the focused Markdown/diff check.
- The user rejected the version 1.0 framing because it behaves mainly as a future template instead of presenting the existing evidence corpus.
- Confirmed product decision: 343 prompts are the raw universe to filter; the filtered catalog must remain inside this single complementary annex so the submission does not gain two additional annexes.
- Revised target: explain the Gentle AI + Engram Cloud team workflow, show substantive prompts and their session/observation/decision context, and document exclusions for vague or operational prompts.
- Reconnection with the existing private Cloud token succeeded for authenticated status: 80 local chunks, 382 remote chunks, and 308 pending imports were reported.
- The authorized import attempt stopped before mutation because the Cloud peer advertises manifest version 1 while the local Engram v2.0.0 database contains project-owned sessions; protocol downgrade is unsupported.
- Read-only incident diagnosis confirmed the local baseline remained 111 sessions, 391 observations, and 329 prompts; no import occurred.
- The user decided to proceed with the 329 locally verifiable prompts rather than delay the annex for a Cloud server upgrade.
- The annex must disclose that 343 was the reported Cloud universe, 329 prompts were reproducibly available at evidence closure, and 14 reported prompts could not be recovered because of the protocol incompatibility.
- Four independent classifiers reviewed the frozen 323-prompt corpus in batches. Their preliminary work identified substantive FEP tasks, evidence decisions, artifact requests and validations separately from operational, vague and duplicate prompts.
- Because one preliminary batch omitted records while another overlapped records, the final writer reclassified the frozen corpus directly from a project-scoped read-only database query.
- T3 completed: 323 prompts were reproducibly classified as 173 `SUSTANTIVO`, 56 `OPERATIVO`, 85 `VAGO`, 9 `DUPLICADO`, and 0 `AJENO`.
- T4 completed: the single annex was replaced with an evidence-first dossier containing all 173 substantive prompt records, their stable IDs, timestamps, sessions, prompt text, and linked observation titles where available.
- The writer excluded 12 absolute local paths for privacy; no credential values required redaction.
- T5 initially failed: 11 of 20 deterministic sampled catalog records omitted observation titles present in SQLite. Text, timestamps, session IDs, catalog membership, category arithmetic, privacy scan, and academic safeguards passed.
- Bounded T4 correction completed: all 173 observation-title mappings were regenerated directly from the frozen SQLite query; the writer verification reported 0 mismatches. The classification rule is now documented as auditable, with its historical limitation stated explicitly.
- T5 completed: post-correction independent verification passed with 0 mismatches across all 173 catalog records against the frozen SQLite source; categories sum to 323 and privacy scan found no secrets or absolute home paths.
- The later commit-only verifier was discarded because its brief incorrectly expected an initial addition relative to `master` to be a formatting-only diff; it found no document defect.
- Next step: create the approved issue and single size-exception PR toward `master`.

## Verification evidence

### T1 writer verification

- `test -s 'Anexo Complementario de Trazabilidad de Uso de IA - ONEBYTE - TI-06.md'`: passed.
- Required-term grep for inventory counts, platforms, validation, and human authorship: passed.
- `git diff --check -- 'Anexo Complementario de Trazabilidad de Uso de IA - ONEBYTE - TI-06.md'`: passed.
- `git status --short`: showed the new annex plus the pre-existing unrelated modification and this ODD task file.

### T2 independent verification

- Result: PASS; no blocking findings.
- Confirmed the annex supplements rather than replaces the mandatory form.
- Confirmed coverage of effective prompts, traceable exports/links, version history, section-level declarations, individual declarations, human-only safeguards, evidence states, and bidirectional reconciliation.
- Confirmed aggregate Engram counts remain contextual and explicitly unverified.
- Parent resolved the verifier's PDF-text limitation using the text extraction already obtained from the governing PDF in this session.
- Parent spot check: `git diff --check` and focused required-term grep both passed.
- Remaining gaps are real-world data-entry/evidence gaps, not template defects: dated Engram snapshot/export, stable session references, individual responsibility, artifact-to-commit mapping, and named/dated human validation.

### T3 Cloud reconnection incident

- Authentication succeeded using the existing private environment configuration; no credentials were exposed.
- Cloud status reported 382 remote chunks and 308 pending imports for `fep-investigacion`.
- Import failed during protocol negotiation before any chunk transfer: peer manifest version 1 does not support the local project-owned session ownership mode.
- Independent read-only diagnosis confirmed no local mutation: counts remain 111 sessions, 391 observations, and 329 prompts.
- The user explicitly chose the locally verifiable corpus. The final dossier uses the reproducible pre-annex 323-prompt snapshot and documents the reported 343-prompt Cloud count as unreconciled.

### T3/T4 writer verification

- Frozen corpus query: 323 rows.
- Final categories: 173 `SUSTANTIVO`, 56 `OPERATIVO`, 85 `VAGO`, 9 `DUPLICADO`, 0 `AJENO`; sum = 323.
- Full catalog: 173 substantive records.
- `git diff --check` passed for the annex.
- Independent T5 result: FAIL due to 11 of 20 sampled observation-title mapping discrepancies; all sampled prompt text, timestamps and session IDs matched.
- Correction completed by the writer: source=323, categories=323, catalog=173; complete catalog-to-SQLite observation mapping mismatches=0; privacy scan found no sensitive matches.
- T5 post-correction verification: PASS. Source=323; categories sum=323; catalog=173; all catalog fields and observation-title multisets matched SQLite with 0 mismatches.
- `git diff --check` passed and privacy scan found no secret/private-key/password/token values or absolute home paths.
- The subsequent commit-only verifier failed due to its own invalid premise about diff size, not a dossier finding; it confirmed the committed diff had only the authorized annex and ODD task file, no onboarding change.
