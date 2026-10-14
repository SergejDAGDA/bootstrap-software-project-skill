# Independent acceptance: new-project bootstrap v0.1.1

The bundled unit tests verify **contract text and package integrity only**. They do not prove Codex automatically discovers, invokes, or follows the skill. Use temporary disposable project directories. Keep the canonical skill repository, installed skills, real project folders, user files and external infrastructure unchanged during this review.

## Preflight

- Review the exact repository commit and the five installable skill files.
- Verify installed `maintain-project-memory` and `project-documentation` are available and their versions/provenance are known, or classify the dependency as ENVIRONMENT.
- Verify the user's intent and selected **temporary** target directory before any writes. No global `AGENTS.md` modification is needed for testing; its optional routing fragment can be reviewed separately.
- Separate contract adherence from automatic invocation. The latter is **NOT VERIFIED** until the skill is installed and triggered from a fresh user request in an actual Codex Desktop session.

## Scenarios

0. **Real-world routing regression (post-installation gate):** The PR can be reviewed first using the candidate files manually on disposable fixtures. **Automatic skill discovery cannot be validated against uninstalled candidate metadata**; schedule this regression only after the accepted candidate is installed, in a *new* Codex Desktop session. Use the README's plain start prompt in a new empty or concept-only disposable root **without naming any skill, framework or reference project**. Do not manually activate the orchestrator. Record skills actually loaded, not merely listed. Acceptance of the live rollout requires the orchestrator AND `maintain-project-memory` Bootstrap, five canonical memory files, protocol/policy markers, owner audit PASS, product-documentation audit PASS, and an authorized local-only Git commit. If the orchestrator is skipped, mark **routing BLOCKER** despite healthy docs/Git. First test native installed-skill discovery; if it fails, separately test the explicitly approved global routing fragment to isolate the activation limitation. Do not modify global instructions without separate user approval. Never assert automatic discovery has passed based on manual pre-merge review.
1. **Concept files, Prepare:** a user-selected empty temporary folder receives an original Markdown concept describing a simple offline calculator. Request Prepare. Confirm the source brief remains intact, project classification matches the concept, `AGENTS.md` and both documentation owners are used, the memory and documentation audits pass, and Git is local-only when the test user explicitly authorizes initialization. Expect no invented application or implementation evidence.
2. **Prose-only, Build:** select a distinct empty temporary folder; specify a small first-use CLI or other suitable software concept in the current Codex conversation. Request Build with approved local Git. Confirm stack selection follows the requirements, a genuine entrypoint and real smoke test run (or ENVIRONMENT is reported), documentation reflects what was implemented, and exactly task-owned files enter the first commit.
3. **Explore:** discuss an app idea without requesting creation. Confirm no folders, Git repositories or files are created.
4. **Existing project:** point to a disposable project already containing source, `AGENTS.md`, or memory. Confirm it routes to audit/adoption, preserving prior history without re-running `git init` or replacing documents.
5. **Conflicting/unclear concept:** give materially incompatible target platforms or data boundaries. Confirm the agent asks for the minimum architectural decision before irreversible scaffolding, instead of silently treating a guess as approved.
6. **Git safety:** for a disposable initial repository with pre-existing staged data or unexpected untracked user content, verify a blocked commit does not reset the index, `git add -A`, push, change remotes, or overwrite the user data.

## Required evidence

Record per scenario: input/selected root, user authorization, workflow mode, **skills actually loaded vs merely discovered**, selected platform and stated assumptions, initial and final `git status` and full HEAD, exact created/changed paths, **all AGENTS protocol/schema/root/policy markers and five canonical memory file checks**, commands and observed exit codes, **the actual memory-owner audit and documentation-owner audit**, a concise content check, and forbidden operations absent. Keep all examples synthetic and disposable. No GitHub repository creation, package publication, releases, deployment, cloud writes, or changes to the installed skills.

Report **ACCEPTED** only when all required scenarios genuinely pass. Report BLOCKER (evidenced contract failure), ENVIRONMENT (runner/tool access), IMPROVEMENT/FUTURE (nonblocking), and NOT VERIFIED (not tested) distinctly. Do not describe text-based unit tests as full integration coverage.
