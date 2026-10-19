# Bootstrap Software Project

[Русский](README.ru.md)

A portable Agent Skill for Codex Desktop that starts **any kind of new software project** from a concept: a website, web app, desktop Windows/macOS/Linux application, calculator, CLI, library, service, extension, or a hybrid. The skill classifies the intended product and selects appropriate foundations instead of assuming one technology stack.

**Installable skill version:** `0.1.3`. The skill preserves Git identity preflight, owner-specific completion gates, and conditional cross-project release/deployment routing. Published release and installed versions must be verified independently.

**Repository versus skill identity:** The GitHub distribution repository is `SergejDAGDA/bootstrap-software-project-skill`, while the installed Agent Skill remains `bootstrap-software-project` (directory `skills/bootstrap-software-project/`, frontmatter `name`, and invocation `$bootstrap-software-project`). The `-skill` suffix belongs to the repository name only; it is **not** part of the skill ID. Other agent runtimes are not claimed as tested.

## What it coordinates

- Concept/MVP input from Markdown documents, the current task, or both; no compulsory formal PRD.
- Project type/platform inference and clarifications for only material ambiguities.
- `maintain-project-memory` Bootstrap: canonical `AGENTS.md` and `docs/project-memory/`.
- `project-documentation` init: a durable root README and `docs/project-knowledge/`, based on real scope/evidence.
- The platform's ordinary generators/SDKs, `.gitignore`, and executable smoke checks for Build mode.
- An approved **local** Git repository, safe initial commit, and no implied remote publication.

The skill is an **orchestrator**, not a replacement for either companion skill. **The installable `SKILL.md` defines the workflow; `agents/openai.yaml` only points to it and must not define alternate fallback rules.** **Installed companions remain authoritative:** when `maintain-project-memory` is installed, Prepare and Build require five canonical memory files, `AGENTS.md` protocol/policy markers and a passing owner audit; likewise for an installed `project-documentation`. An installed-but-failing owner is a **BLOCKER**, never a reason to silently switch modes. **Without optional companions**, a *standalone* baseline can complete with ordinary project notes/Markdown and native checks, without pretending to implement another skill's schema or audit. Explicitly required missing protocols block completion.

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
- **Prepare:** verified concept, agreed constraints, durable project context, documentation and local history; canonical owner outputs if installed, clearly labeled standalone notes otherwise (a **mixed** case is supported when only one owner is installed).
- **Build:** Prepare plus the smallest runnable/useful application skeleton, verified with real commands.
- **Existing project:** existing source/config, maintained project rules (including project-local `AGENTS.md`), or project memory route to adoption/update without reinitialization.

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

## Git identity without a hosting account

Git commits require author and committer name/email, but **not** GitHub, GitLab or a remote. During the early preflight, Bootstrap checks explicit effective Git config and authorized environment overrides; guessed OS/hostname identities do not count. If either identity is missing, Codex asks once for name/email and whether to configure only this repository or globally. Global changes require separate consent. An email is commit metadata, not a login or necessarily a live inbox. Never hardcode users' identities or fabricate a service-specific `noreply` address. Files and the index are preserved if identity is unresolved.

## Pre-existing files and selective tracking

An empty or concept-only folder (including briefs, supplied SVG/design files) is eligible. Existing application code, maintained project memory or substantive configuration triggers an **existing-project** route. Unknown, sensitive, oversized, binary or license-uncertain material is reviewed, preserved and not automatically staged. Presence of a file does not authorize modifying or committing it.

## Local Git policy

Local Git is the **default intended outcome** for a new full-fledged software project, including projects never published online. Installing a skill from GitHub does not require Git in that project's folder.

`git init` needs explicit authorization: this can be granted once as a standing instruction for user-nominated new-project folders by adopting the [optional global routing fragment](docs/OPTIONAL_GLOBAL_ROUTING.md), or in the specific project request. `Local Git commit policy: auto` authorizes scoped local commits **after** a repository exists; it is not, by itself, consent to initialize Git. No `push`, remote repository creation, CI provider provisioning, release, or deployment is implied.

## Test

```bash
python -m unittest discover -s tests -v
```

Contract tests cover skill/package structure, trigger guardrails, project-type adaptability, documented Git safety, and absence of conflict with existing memory and documentation ownership. They are **not** an end-to-end Codex invocation test.

## Acceptance and regression

See [independent acceptance](docs/ACCEPTANCE.md), including a **plain-prompt fresh Desktop** scenario that must distinguish automatic activation from manual invocation. A first local commit **with an installed memory owner but without its canonical gate** is a failed Bootstrap. Without that optional owner, the standalone baseline follows its own explicit acceptance criteria. Contract tests do not establish agent behavior. Independent source acceptance precedes merge/install; automatic trigger validation follows installation in a fresh Desktop session.
