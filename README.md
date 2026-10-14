# Bootstrap Software Project

[Русский](README.ru.md)

A portable Codex Agent Skill for starting **any kind of new software project** from a concept: a website, web app, desktop Windows/macOS/Linux application, calculator, CLI, library, service, extension, or a hybrid. The skill classifies the intended product and selects appropriate foundations instead of assuming one technology stack.

**Version:** `0.1.1` patch candidate, pending independent source acceptance and local reinstall. `v0.1.0` passed isolated manual tests but a real fresh-folder Prepare request revealed that an agent can select documentation and Git workflows **without loading the bootstrap orchestrator**, leaving project memory absent while declaring the work complete. This update adds a mandatory memory completion gate and stronger routing guidance; true automatic activation still needs a fresh Desktop test.

## What it coordinates

- Concept/MVP input from Markdown documents, the current task, or both; no compulsory formal PRD.
- Project type/platform inference and clarifications for only material ambiguities.
- `maintain-project-memory` Bootstrap: canonical `AGENTS.md` and `docs/project-memory/`.
- `project-documentation` init: a durable root README and `docs/project-knowledge/`, based on real scope/evidence.
- The platform's ordinary generators/SDKs, `.gitignore`, and executable smoke checks for Build mode.
- An approved **local** Git repository, safe initial commit, and no implied remote publication.

The skill is an **orchestrator**, not a replacement for either companion skill. **Prepare and Build are incomplete without the five canonical project-memory documents, required `AGENTS.md` markers/policies, and a passing owner memory audit**; a product-documentation audit and clean commit cannot substitute for them. If a companion is unavailable, the workflow reports that its ownership layer is not fully verified rather than claiming complete readiness.

## Start a new project (copy and adapt)

Use a fresh Codex Desktop chat in the selected project folder. The prompt intentionally does **not** name Agent Skills, Git commands, a technology stack or another reference project. Place your `CONCEPT.md` there if available; otherwise put the idea directly in the request.

```text
Start a new standalone software project.
Project folder: <PROJECT_FOLDER_PATH>

Read any concept or MVP documents in this folder. If none are present,
here is my concept: <SHORT_CONCEPT_DESCRIPTION>

First, prepare the project for development: assess the concept, identify
the project type, propose an architecture, MVP and testable development
plan, and create the necessary durable project files and guidance.
Do not implement the application yet. Ask about architectural decisions
only where requirements do not determine a safe answer.

I authorize standard local Git initialization and a safe first local
commit in this selected new project folder. Do not create a remote,
push, publish, release or deploy. Preserve all existing source documents.
At the end, report what was created, what was verified, and what remains
unresolved. Do not call the project ready if required preparation is missing.
```

For Build, replace "Do not implement the application yet" with a request
for the smallest working app and real smoke tests. A general idea-only
conversation does not imply permission to create files. Since implicit skill
discovery is not guaranteed, the [optional global Codex routing rule](docs/OPTIONAL_GLOBAL_ROUTING.md)
can be added **only after explicit review and approval**; never silently
edit a user's global `AGENTS.md`.

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

## Acceptance and regression

See [independent acceptance](docs/ACCEPTANCE.md), including a **plain-prompt fresh Desktop** scenario that must distinguish automatic activation from manual invocation. A first local commit without canonical project memory is a **failed Bootstrap**, not an accepted documentation-only variant. Contract tests do not establish agent behavior. Independent source acceptance precedes merge/install; automatic trigger validation follows installation in a fresh Desktop session.
