# First-run, Git, and acceptance boundaries

## Eligible target

Use the **single project-root eligibility rule** in `SKILL.md` > Route the request. Empty or concept-only roots (including supplied design assets) and blank clean Git roots are eligible. Source code, substantive configuration, project memory, or project-local `AGENTS.md` with maintained rules signals **existing project**; do not bootstrap over it. A valid empty Git root is reusable, never a reason to re-run `git init`. Resolve ambiguous files before writing.

Before writing:

- Resolve and display the real target path. Reject guessed paths and paths that could traverse into unapproved directories.
- Verify the folder exists or ask before creating it; inspect hidden files and symlinks/reparse points, not just visible entries.
- Determine whether this root or an ancestor already belongs to a Git worktree via real Git commands. Do not `git init` inside another repository by default; never `git init` at its parent by accident.
- Preserve user-supplied briefs and assets byte-for-byte; if edits are contemplated, record pre-write checksums. Do not treat blank folders as permission to create hosting accounts or repositories remotely.
- Classify files before writes under the single eligibility rule: concept/brief/design sources permit concept-only Bootstrap; existing code, substantive config, project-local `AGENTS.md` with maintained rules or maintained memory means **existing project**; binary, oversized, third-party or license-uncertain assets require an explicit selective-tracking decision; unknown, unrelated or sensitive files trigger review and must not enter staging by default. File presence does not equal permission to edit, delete, import or commit.
- Inventory existing files, hidden files and Git staging. Any surprising files or dirty/staged work trigger review, not wholesale regeneration.

## Git identity without an external hosting account

Before bulk scaffolding, establish whether the **effective** author and committer identities are explicitly configured, using Git's repository/global/system/conditional config, any authorized environment overrides and `user.useConfigOnly=true` identity checks. Do not rely on automatic username@hostname guesses, or presume GitHub/GitLab credentials or remotes. Check both author and committer, and re-check immediately before commit.

If absent, pause to ask what name/email to use and whether to set it **locally** for the selected repo or **globally**. Do not silently pick a developer name, an email, a service account or a made-up `noreply` address. A local setting can be applied only after approved `git init`; a global setting requires separate explicit consent, preserves existing settings, and affects future repositories. No identity values belong in a publicly distributed skill or test fixture except obvious generic dummy examples. Report ENVIRONMENT / INCOMPLETE while blocked without discarding draft files, Git index or history. Git author identity is commit metadata, **not** login authorization.

## Git authorization handshake

`maintain-project-memory`'s local commit policy describes **commits**, not authorization for `git init`. Respect that rule.

At the first Bootstrap plan, clearly say that a **new local Git repository and initial commit** are standard outputs. Execute `git init` without an extra prompt only if the user has already explicitly approved this Bootstrap behavior (current request or user-owned standing project-start policy covering the nominated root). Otherwise ask once for authorization; never infer it from a generic cached setting or a random folder. The user may opt out, with reduced readiness reported.

- Prefer Git's supported native commands and standard ignore patterns for the chosen stack.
- Add `.gitignore` before staging: secrets/`.env`, credentials, local databases, backups, runtime, build outputs, node_modules/venvs, and OS-specific files where appropriate. Do not ignore legitimate source data by blindly copying a global template.
- Treat any pre-existing staged changes as a stop for automatic commit; preserve the index. Use explicit reviewed paths rather than `git add .`, `git add -A`, `git commit -a`, or a broad directory sweep.
- Do not set global Git user identity **without explicit consent**, disable hooks, rewrite history, add a remote, or push on behalf of the user.
- Verify new HEAD, committed paths, and remaining unrelated working-tree state.

Downloading tools or installing skills from GitHub may be done by supported installers without Git in the *target project*. That fact does not reduce Git's value as the project's local version history. Do not conflate a GitHub remote with a local Git repository.

## Minimal acceptance for Prepare

**Integrated release gate:** if `maintain-project-memory` is installed/required, absence of canonical project memory is a **BLOCKER**, not an optional follow-up. Before the first task-owned local commit, verify the owner's actual audit succeeds and `AGENTS.md` has the protocol/schema/root/update-policy/commit-policy markers. If an installed owner is broken, do not hide its failure behind standalone fallback. Preserve partial files without calling the result complete.

**Standalone release gate:** if the owner is genuinely absent and not explicitly required, minimal truthful `AGENTS.md` and project notes can pass without any claim to that protocol or its audit. If `project-documentation` is absent, use small native Markdown with explicit link/scope checks; if installed, its actual audit remains mandatory.

- The concept, MVP and exclusions are grounded in supplied evidence.
- Key decisions and unknowns are recorded with correct approval provenance.
- `AGENTS.md` routes future work to installed memory/documentation owners where applicable, or records standalone project rules when absent.
- When the memory owner is installed, all five canonical `docs/project-memory/{PROJECT,STATUS,DECISIONS,SESSION_LOG,HANDOFF}.md` files exist and its actual audit passes; otherwise standalone notes exist without false protocol claims.
- The product documentation has an accurate index, no broken relative links and Git-clean authored Markdown; use the actual owner audit if installed, native checks otherwise.
- The intended project root is recognized correctly; both Git identities are explicitly resolved; local Git exists and first commit is verified when approved.
- The next developer can resume from disk without needing inaccessible previous chat context.

## Additional acceptance for Build

- The selected toolchain matches platform and use case, rather than a hard-coded default.
- The generated entrypoint runs in the current available environment, or the exact environment limitation is documented without claiming success.
- At least one real first-use workflow works; checks/tests assert genuine behavior, not placeholder success.
- Setup/run/verify commands and dependency versions are grounded in actual project files and execution.
- CI only when a real provider and runnable checks justify it; no false green CI claims.

## Common failure outcomes

- `BLOCKER`: required behavior is broken, critical user-data safety missing, or approved scope is violated. Fix before completing.
- `ENVIRONMENT`: needed SDK, permission, Git, compiler, OS, credential or network not available. Preserve partial work; do not fake verification.
- `IMPROVEMENT/FUTURE`: optional additional structure, release automation, CI provider, expansion, tests for unimplemented features. Do not expand scope.
- `NOT VERIFIED`: claim is plausible but not yet demonstrated. Report uncertainty.

## Idempotence

If Bootstrap is retried, re-evaluate the directory and active policy. A prior successful Bootstrap turns the directory into an **existing project**. Prefer adoption or a normal new feature request rather than duplicating docs, rewriting decisions, `git init` again, or changing source code to match a stale initial concept.
