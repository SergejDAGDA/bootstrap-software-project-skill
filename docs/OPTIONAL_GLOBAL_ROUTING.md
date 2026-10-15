# Optional global Codex routing (requires user review)

The skill can activate implicitly based on its `description`, but implicit selection is **not guaranteed**. A fresh real-world Prepare attempt selected documentation/planning/Git skills while skipping both this orchestrator and canonical project-memory Bootstrap. A short, **user-reviewed** global `~/.codex/AGENTS.md` rule is the preferred persistent mitigation when the user needs reliable routing before a project-local `AGENTS.md` exists. Changing the installed skill alone cannot force an agent to load that skill in a turn where it was not selected.

**Do not overwrite an existing global `AGENTS.md`.** Read, reconcile and append only after explicit user approval. This snippet grants permission for **local** Git initialization only under the stated narrow conditions. It does not authorize publishing.

Suggested English fragment:

```markdown
## Starting a new software project

When I explicitly ask to create, initialize, prepare, design the initial architecture/MVP and working documentation of, or start building a substantial NEW software project in an empty or concept-only folder I selected, use the installed `bootstrap-software-project` skill as the coordinating workflow BEFORE separately choosing planning, documentation or Git workflows. Infer project type and platform from my concept/Markdown docs; ask only about material unresolved architectural choices. Do not trigger Bootstrap on brainstorming, read-only reviews, or already-initialized existing projects.

For a genuinely new project folder I explicitly selected for Bootstrap, I authorize native local `git init` and one safe first local Git commit as part of that workflow. This standing permission does not cover existing projects, directories within other Git repositories, user-data folders, cloud services, remote Git operations, releases, or deployment. The agent must first inspect the target directory, preserve existing content, and follow the skill's safety gates.

Use installed `maintain-project-memory` and `project-documentation` as owners of their canonical files. Require owner audits and canonical project-memory markers/files when those owners are installed. When genuinely absent, use Bootstrap's documented standalone baseline and native checks; never claim owner compatibility. Never bypass an installed-but-failing owner. Preflight effective Git author and committer identity early; if missing, ask the user for commit name/email and local/global config scope. Do not assume a GitHub account. Follow project-local `AGENTS.md` thereafter. Never infer publishing permission from local Git use.
```

If the user does not approve this standing permission, leave it out. The Bootstrap skill will then present local Git initialization for one-time approval as part of the first-project plan.
