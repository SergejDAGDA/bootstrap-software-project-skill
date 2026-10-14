# Optional global Codex routing (requires user review)

The skill can activate implicitly based on its `description`, but implicit selection is not an absolute execution guarantee. A short, **user-reviewed** global `~/.codex/AGENTS.md` fragment can make the start-of-project contract clearer before project-local instructions exist.

**Do not overwrite an existing global `AGENTS.md`.** Read, reconcile and append only after explicit user approval. This snippet grants permission for **local** Git initialization only under the stated narrow conditions. It does not authorize publishing.

Suggested English fragment:

```markdown
## Starting a new software project

When I explicitly ask to create, initialize, prepare, or start building a substantial new software project in a folder I have selected, route the task through the installed `bootstrap-software-project` skill. Infer project type and platform from my concept/Markdown docs; ask only about material unresolved architectural choices. Do not trigger Bootstrap on idea brainstorming alone.

For a genuinely new project folder I explicitly selected for Bootstrap, I authorize native local `git init` and one safe first local Git commit as part of that workflow. This standing permission does not cover existing projects, directories within other Git repositories, user-data folders, cloud services, remote Git operations, releases, or deployment. The agent must first inspect the target directory, preserve existing content, and follow the skill's safety gates.

Use installed `maintain-project-memory` and `project-documentation` for their respective canonical files, rather than duplicating their ownership. Follow project-local `AGENTS.md` thereafter. Never infer publishing permission from local Git use.
```

If the user does not approve this standing permission, leave it out. The Bootstrap skill will then present local Git initialization for one-time approval as part of the first-project plan.
