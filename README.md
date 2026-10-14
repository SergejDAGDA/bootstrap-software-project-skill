# Bootstrap Software Project

[Русский](README.ru.md)

A portable Codex Agent Skill for starting **any kind of new software project** from a concept: a website, web app, desktop Windows/macOS/Linux application, calculator, CLI, library, service, extension, or a hybrid. The skill classifies the intended product and selects appropriate foundations instead of assuming one technology stack.

**Status:** version `0.1.0` development candidate, **not published or installed**. This package defines the workflow and static contract checks; it has not yet passed an independent real Codex Desktop new-folder acceptance.

## What it coordinates

- Concept/MVP input from Markdown documents, the current task, or both; no compulsory formal PRD.
- Project type/platform inference and clarifications for only material ambiguities.
- `maintain-project-memory` Bootstrap: canonical `AGENTS.md` and `docs/project-memory/`.
- `project-documentation` init: a durable root README and `docs/project-knowledge/`, based on real scope/evidence.
- The platform's ordinary generators/SDKs, `.gitignore`, and executable smoke checks for Build mode.
- An approved **local** Git repository, safe initial commit, and no implied remote publication.

The skill is an **orchestrator**, not a replacement for either companion skill. If a companion is unavailable, the workflow reports that its ownership layer is not fully verified rather than claiming complete readiness.

## Modes

- **Explore:** no project creation merely because an idea was discussed.
- **Prepare:** verified project concept, approved constraints, source map, memory, documentation, and local history; implementation can wait.
- **Build:** Prepare plus the smallest runnable/useful application skeleton, verified with real commands.
- **Existing project:** route to adoption/update instead of reinitializing or overwriting.

## Structure

```text
skills/bootstrap-software-project/
  SKILL.md
  VERSION
  agents/openai.yaml
  references/project-assessment.md
  references/first-run-safety.md
tests/test_skill_contract.py
docs/OPTIONAL_GLOBAL_ROUTING.md
```

Only `skills/bootstrap-software-project/` is the installable skill. Repository-level docs and tests stay outside it.

## Local Git policy

Local Git is the **default intended outcome** for a new full-fledged software project, including projects never published online. Installing a skill from GitHub does not require Git in that project's folder.

`git init` needs explicit authorization: this can be granted once as a standing instruction for user-nominated new-project folders by adopting the [optional global routing fragment](docs/OPTIONAL_GLOBAL_ROUTING.md), or in the specific project request. `Local Git commit policy: auto` authorizes scoped local commits **after** a repository exists; it is not, by itself, consent to initialize Git. No `push`, remote repository creation, CI provider provisioning, release, or deployment is implied.

## Test

```bash
python -m unittest discover -s tests -v
```

Contract tests cover skill/package structure, trigger guardrails, project-type adaptability, documented Git safety, and absence of conflict with existing memory and documentation ownership. They are **not** an end-to-end Codex invocation test.

## Planned acceptance

Use a fresh **disposable** folder with an explicit Prepare request and a supplied Markdown concept; repeat with a Build request in a new folder and a prose-only concept. A third test should ask only to brainstorm (zero filesystem writes). Verify existing-project safety, authorized local Git, documented artifacts, meaningful tests, and no remote changes. Review blockers independently before publishing or installing.
