---
name: bootstrap-software-project
description: Bootstrap a substantial NEW software project from chat ideas or Markdown concept/MVP documents. Use when asked to create, set up, scaffold, prepare or start building a website, web app, Windows/macOS/Linux desktop program, CLI, calculator, library, service, extension or other software. Classify type and platform, coordinate memory/documentation and native tooling, initialize authorized local Git, and verify the baseline. Not for brainstorming alone or changes in existing projects.
---

# Bootstrap Software Project

Create the **smallest complete, reproducible starting state** for a genuinely new software project. Adapt to the concept and intended platform rather than imposing a framework, language, server, CI provider, or directory tree. The skill **coordinates** existing tools and skills; it is not a generic code generator, memory writer, or release system.

## Route the request

1. **Explore only:** If the user is discussing an idea, comparing options, or expressly avoiding implementation, do not create files, initialize Git, or silently turn the conversation into a project. Help explore using ordinary conversation.
2. **Prepare:** If asked to prepare a project, concept, specification, or development foundation, produce the approved project baseline and working documentation. A runnable app is not required.
3. **Build:** If asked to create/build a new application or usable initial prototype, do Prepare and then a minimal runnable application skeleton with real launch and verification commands. Do not claim it runs unless actually executed.
4. **Existing project:** If the target already has meaningful implementation or project memory, stop *new-project initialization*. Route to existing-project adoption/update workflows; preserve files and Git history. This skill may report a proposed migration, but never re-bootstrap over existing user work.

The user's explicit task and approved scope outrank these defaults. Ask **only** for missing choices that materially change the architecture, storage/security boundary, target platform, distribution model, or first useful outcome. If several decisions are needed, present a compact proposed baseline and ask approval of those decisions together. Don't demand a formal specification from an informal concept.

## Establish input, authority, and target

- Determine the intended project root from an explicit user-selected folder/workspace. Do not guess a writable destination. Resolve the real path and inspect contents and enclosing version-control roots before writes. A truly empty directory, a concept-only directory, or an otherwise blank clean Git repository rooted exactly there can be new projects; preserve supplied source documents and existing history.
- Gather a **bounded** input pack from files in that folder and the current Codex conversation: concept, MVP, sketches, constraints, expected usage, target platforms, relevant decisions. Include user-provided Markdown and ordinary prose equally. Never claim to see another ChatGPT/Codex conversation unless its content was supplied or an authorized connector actually retrieved it.
- Order authority: current user direction and project rules; explicitly approved concept/MVP decisions; other supplied requirements; current implementation evidence; provisional ideas. Record uncertain claims as Proposed, Unverified, or Open — not silently Approved.
- Determine product shape, supported platforms, users, interaction model, network/offline needs, data persistence, sensitivity, packaging/distribution, operational footprint, and MVP boundary. The categories are **axes**, not fixed stack presets: see `references/project-assessment.md`.
- Prefer established native platform tooling and reusable/open-source components to invented infrastructure. Verify current compatibility when online sources are available. If unavailable, make dependencies/assumptions explicit and avoid fabricated version claims.

## Make a small bootstrap contract

Before substantial writes, state: (a) project root and whether it is empty/concept-only; (b) Prepare or Build; (c) inferred project type and target platforms; (d) proposed MVP, exclusions, main technical choices and unresolved blockers; (e) Git initialization/commit authorization; (f) checks that will establish success. Ask for approval only where the user's previous instructions do not establish the necessary consent. This is not permission to publish or deploy.

Read `references/first-run-safety.md` for filesystem/Git safety and the minimal completion contract. Do not change global `~/.codex/AGENTS.md`, an existing project's `AGENTS.md`, user credentials, cloud resources, or package registries without separately applicable authority.

## Execute by ownership and in order

1. **Inspect and classify.** Read only relevant inputs, inventory the target folder and possible parent Git root, resolve critical choices. Preserve the raw concept documents as supplied; use citations or relative source pointers where practical. Explicitly inventory which pre-existing briefs may be tracked in the first commit; do not silently stage them, and flag any untracked nonportable sources on which the durable project documents depend. Do not copy personal or externally licensed material into new repositories without permission.
2. **Establish local Git.** A new full-fledged project should use Git by default. **`Local Git commit policy: auto` does not itself authorize `git init`.** Initialize Git only when the user has explicitly approved this new-project bootstrap including its default local Git behavior, or approved Git initialization for this target. Such approval may be a standing instruction for the user's nominated new-project folders. If absent, present it as a standard part of the bootstrap contract and obtain consent before executing. When a clean Git repository already exists at the exact intended root, reuse it without re-running `git init`; inspect HEAD/index/branch first. Never initialize an enclosing workspace or nested repository by accident. Use native Git; never create a GitHub remote implicitly.
3. **Create project memory through its owner.** If installed and write-eligible, invoke `maintain-project-memory` **Bootstrap**. Use its current approved template and update policy; create/merge project-local `AGENTS.md` and canonical `docs/project-memory/` files. New projects that approve the standard workflow may adopt `Local Git commit policy: auto`; keep this separate from the memory update policy. Do not invent approval provenance or alter decision history. If the companion skill is unavailable, use a minimal clearly marked provisional coordination baseline and report that canonical memory Bootstrap still needs its owner; do not claim full completion.
4. **Create product documentation through its owner.** If installed, invoke `project-documentation` **init** to document real requirements and accepted design, using `docs/project-knowledge/` by default. Create an accurate root `README.md`; do not generate API, schema, or release documentation for nonexistent implementation. Run the current documentation audit, including its Git-whitespace gate for authored Markdown. If unavailable, record the dependency gap; do not mislabel invented prose as verified product contracts.
5. **Create technical foundation (Build only).** Choose the simplest mature platform-native generator or existing template appropriate to the accepted project shape, then scaffold the least useful runnable slice. Create an appropriate `.gitignore` before staging anything. Use deterministic dependency files/lockfiles where supported. Add clear local setup/run/test commands; use actual smoke tests. CI configuration is appropriate only when real executable checks and a chosen provider exist; do not invent passing CI or assume GitHub publication.
6. **Verify and checkpoint.** After Build, route an evidence-based product-documentation **update** through `project-documentation` so that docs reflect what actually runs, not just the initial plan. Check entrypoint/run instructions, actual tests where available, relevant security/data boundaries, documentation links and Git whitespace, project-memory audit, and precise changed-file scope. Reconcile any failures before asserting readiness. Have the memory owner record one factual completed checkpoint, distinguishing repository/source revision from deployment/runtime identity.
7. **Make a scoped local commit.** Follow `maintain-project-memory`'s `references/local-git-checkpoints.md` when available. Stage only reviewed task-owned paths, verify cached diff and `git diff --cached --check`, then commit once if authorized and safe. Existing staged work, changing HEAD, ambiguous ownership, secrets, or failed checks **stop** the commit. Never bypass hooks or clean/reset unrelated files. No push, remote repo, tag, release, installer publication or deployment.

## Completion states

- **PREPARED:** approved scope, project-owned memory/knowledge, and truthful next action exist; a runnable app may not exist. Report Git status separately.
- **BUILD READY:** the intended minimal application actually starts or runs and available checks pass, with documented dependencies and development commands.
- **INCOMPLETE / ENVIRONMENT:** missing approvals, Git/tools, broken checks, unclear ownership, or blocked runtime prevent a claimed outcome. Preserve partial artifacts and report the exact next safe action. A clean documentation audit alone does not prove a runnable application.

For the standard full-project bootstrap, consider the local Git repository and first safe local commit part of readiness unless the user expressly opted out. No remote service activity is ever implied.

## Final report

Include: inferred project type/platform, Prepare/Build result, MVP scope and key decisions/assumptions, created files (briefly), invoked companion skills or fallback, real commands/checks and outcomes, Git root/branch/local SHA and remaining dirty files, unverified/external dependencies, and the next safe step. Distinguish proposed, written, tested, committed, published, installed and running states. Do not write a success claim before actually validating it.
