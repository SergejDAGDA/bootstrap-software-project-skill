# First-run, Git, and acceptance boundaries

## Eligible target

A **new** project root is either empty, contains only user-provided concept/brief material, or is an otherwise blank pre-initialized Git repository rooted at the exact selected folder with no conflicting history or project implementation. Treat a folder with meaningful source code, project configuration, maintained AGENTS rules, or project memory as an **existing** project, not as an empty Bootstrap target. A valid empty Git root is reusable, never a reason to re-run `git init`.

Before writing:

- Resolve and display the real target path. Reject guessed paths and paths that could traverse into unapproved directories.
- Verify the folder exists or ask before creating it; inspect hidden files and symlinks/reparse points, not just visible entries.
- Determine whether this root or an ancestor already belongs to a Git worktree via real Git commands. Do not `git init` inside another repository by default; never `git init` at its parent by accident.
- Preserve user-supplied briefs. Do not treat blank folders as permission to create hosting accounts or repositories remotely.
- Inventory existing files. Any surprising files or dirty/staged work trigger review, not wholesale regeneration.

## Git authorization handshake

`maintain-project-memory`'s local commit policy describes **commits**, not authorization for `git init`. Respect that rule.

At the first Bootstrap plan, clearly say that a **new local Git repository and initial commit** are standard outputs. Execute `git init` without an extra prompt only if the user has already explicitly approved this Bootstrap behavior (current request or user-owned standing project-start policy covering the nominated root). Otherwise ask once for authorization; never infer it from a generic cached setting or a random folder. The user may opt out, with reduced readiness reported.

- Prefer Git's supported native commands and standard ignore patterns for the chosen stack.
- Add `.gitignore` before staging: secrets/`.env`, credentials, local databases, backups, runtime, build outputs, node_modules/venvs, and OS-specific files where appropriate. Do not ignore legitimate source data by blindly copying a global template.
- Treat any pre-existing staged changes as a stop for automatic commit; preserve the index. Use explicit reviewed paths rather than `git add .`, `git add -A`, `git commit -a`, or a broad directory sweep.
- Do not set global Git user identity, disable hooks, rewrite history, add a remote, or push on behalf of the user.
- Verify new HEAD, committed paths, and remaining unrelated working-tree state.

Downloading tools or installing skills from GitHub may be done by supported installers without Git in the *target project*. That fact does not reduce Git's value as the project's local version history. Do not conflate a GitHub remote with a local Git repository.

## Minimal acceptance for Prepare

**Release gate:** absence of canonical project memory is a **BLOCKER**, not an optional follow-up. Before the first task-owned local commit, verify the skill owner's actual memory audit succeeds and `AGENTS.md` has all protocol/schema/root/update-policy/commit-policy markers. If this gate fails, preserve partial files without committing them as a completed Bootstrap, and explain the precise corrective action. If the user explicitly opted out of project memory, report an incomplete/nonstandard setup rather than mislabeling it PREPARED.

- The concept, MVP and exclusions are grounded in supplied evidence.
- Key decisions and unknowns are recorded with correct approval provenance.
- `AGENTS.md` routes future work to project memory and knowledge owners.
- All five canonical `docs/project-memory/{PROJECT,STATUS,DECISIONS,SESSION_LOG,HANDOFF}.md` files exist, and the installed `maintain-project-memory` audit passes with its actual output recorded.
- The product documentation has an accurate index, no broken relative links, and Git-clean authored Markdown.
- The intended project root is recognized correctly; local Git exists and first commit is verified when approved.
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
