# Adaptive project assessment

This is a **decision aid**, not a fixed menu of frameworks or required questionnaire. A single project can combine several categories. Identify the smallest useful outcome and only then select a technical base.

| Possible shape | Look for in the concept | Critical choices to resolve when not evident | Likely native foundation (examples, not mandates) |
|---|---|---|---|
| Informational website / landing page | Mostly published content and navigation | Content editing, localization, static vs dynamic publishing | Static HTML/CSS, native static-site tools; no database by default |
| Interactive website / web app | User workflows, calculations, accounts, collaboration | Client-only vs server, identity, data ownership, offline | Browser UI + only the backend/storage actually needed |
| Calculator / focused tool | Deterministic inputs and outputs, possible standalone UX | In-browser, CLI, desktop, batch; persistence needed? | Small native/library core with thin appropriate UI |
| Windows/macOS/Linux desktop app | Native window, local files, OS integrations, installer | Target OS versions, native vs cross-platform, packaging, auto-updates | Platform-native SDK/toolchain or a justified mature cross-platform framework |
| CLI or automation | Arguments, file transforms, scheduled operation | Shell/OS support, files and destructive safety, distribution | Native language package, CLI argument parser, executable test harness |
| Library / SDK | Reusable API imported by another application | Target language/ecosystem, public API and versioning | Native package layout, unit tests, examples only if used |
| Server / API / service | Network endpoints, background jobs, integrations | Auth, data retention, hosting, secrets, observability | Minimal mature server stack with environment-local setup |
| Mobile app / extension / plugin | Store/client host and platform API | Exact platform and distribution rules, permissions | Official platform SDK and packaging tools |
| Multi-component / hybrid | Several of the above with shared data | True independent deployment boundaries and data contracts | Begin with a simple repository structure; avoid premature microservices |

## Classify along independent dimensions

- **Product**: primary user task, users, minimum completed workflow, expected volume.
- **Execution**: browser, native GUI, CLI, server, library, mobile, hardware, plugin host; multiple are possible.
- **Distribution**: local private use, source checkout, packaged executable, website, app store, service; publishing is always a separate action.
- **Connectivity**: offline first, LAN, public internet, optional sync.
- **Data**: no persistence, local files, database, cloud service; backups, migration, retention where justified.
- **Protection**: public vs private data, authentication/authorization, secrets, external services and trust boundaries.
- **Constraints**: platform/version, licensing, accessibility, deployment environment, skills/budget, maintainability.

## Resolve meaningful ambiguity without burdening the user

1. Infer from concrete scenarios before asking about frameworks or tools.
2. If one product shape clearly follows, explain the inference and proceed within agreed boundaries.
3. If materially different outcomes remain (e.g. offline Windows app vs public multi-user service), ask the **one most consequential question** or show a short baseline with grouped unresolved decisions.
4. Do not ask optional preferences that can be changed later. Record them as assumptions instead.
5. Do not claim the user approved a technical choice merely because it is popular or easiest for the agent.

Examples:

- “Public map with articles and pins” may begin as a browser website; do not assume logins, multi-user editing, or an API.
- “Offline calculator for my Windows PC” requires a local executable/use path; do not default to a hosted web service.
- “Application for Windows and macOS” does **not** by itself prove one cross-platform framework is better; compare packaging and native integrations against the MVP.
- “A script that cleans directories” needs explicit dry-run/destructive boundaries before any tool acts on user files.
