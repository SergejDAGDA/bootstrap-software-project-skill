"""Dependency-free static contract tests for the portable bootstrap skill.

These tests check authorship invariants; they do not simulate Codex behavior.
"""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "bootstrap-software-project"
DOCS = ROOT / "docs"


class BootstrapSkillContractTests(unittest.TestCase):
    def read(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def test_skill_frontmatter_and_name(self):
        text = self.read(SKILL / "SKILL.md")
        self.assertTrue(text.startswith("---\nname: bootstrap-software-project\n"))
        self.assertRegex(text, r"(?m)^description: .*NEW software project")
        self.assertIn("Not for idea-only brainstorming", text)
        self.assertEqual(text.count("\n---\n"), 1)
        description = text.split("\ndescription: ", 1)[1].split("\n---", 1)[0]
        self.assertLessEqual(len(description), 500)

    def test_installable_package_is_minimal(self):
        paths = {p.relative_to(SKILL).as_posix() for p in SKILL.rglob("*") if p.is_file()}
        self.assertEqual(
            paths,
            {
                "SKILL.md",
                "VERSION",
                "agents/openai.yaml",
                "references/project-assessment.md",
                "references/first-run-safety.md",
            },
        )
        self.assertEqual(self.read(SKILL / "VERSION").strip(), "0.1.5")

    def test_trigger_modes_do_not_turn_brainstorming_into_mutations(self):
        text = self.read(SKILL / "SKILL.md")
        for term in ("Explore only", "Prepare", "Build", "Existing project"):
            self.assertIn(term, text)
        self.assertIn("do not create files, initialize Git", text)
        self.assertIn("Don't demand a formal specification", text)

    def test_platform_neutral_and_multiple_project_shapes(self):
        text = self.read(SKILL / "SKILL.md")
        assessment = self.read(SKILL / "references/project-assessment.md")
        for name in ("Windows", "macOS", "CLI", "calculator", "library", "web app"):
            self.assertIn(name, text)
        for name in ("Informational website", "desktop app", "CLI or automation", "Library / SDK", "Server / API", "Mobile app"):
            self.assertIn(name, assessment)
        self.assertIn("not a fixed menu of frameworks", assessment)

    def test_dependency_ownership_and_fallback_are_explicit(self):
        text = self.read(SKILL / "SKILL.md")
        self.assertIn("maintain-project-memory", text)
        self.assertIn("project-documentation", text)
        self.assertIn("docs/project-memory/", text)
        self.assertIn("docs/project-knowledge/", text)
        self.assertIn("standalone mode", text)
        self.assertIn("is **not installed**", text)
        self.assertIn("do not silently downgrade", text)
        self.assertIn("do not generate API, schema, or release documentation", text)

    def test_git_init_is_different_from_local_git_auto_commit(self):
        text = self.read(SKILL / "SKILL.md")
        safety = self.read(SKILL / "references/first-run-safety.md")
        router = self.read(DOCS / "OPTIONAL_GLOBAL_ROUTING.md")
        self.assertIn("does not itself authorize `git init`", text)
        self.assertIn("explicitly approved", text)
        self.assertIn("never `git init` at its parent", safety)
        self.assertIn("git diff --cached --check", text)
        self.assertIn("remote Git operations", router)
        self.assertIn("Do not overwrite an existing global `AGENTS.md`", router)
        self.assertIn("project folder I explicitly selected", router)

    def test_generated_agents_uses_durable_routing_not_transient_phase(self):
        skill = self.read(SKILL / "SKILL.md")
        step = skill.split("3. **Establish durable project context.**", 1)[1].split(
            "\n4. **Create product documentation.**", 1
        )[0]
        for required in (
            "For newly written `AGENTS.md`",
            "not a live progress snapshot",
            "current PREPARE/BUILD phase",
            "pending Git commit",
            "memory owner's `STATUS.md`",
            "remains true after the intended local commit",
        ):
            self.assertIn(required, step)

    def test_verification_and_completion_are_not_faked(self):
        text = self.read(SKILL / "SKILL.md")
        for phrase in ("PREPARED", "BUILD READY", "INCOMPLETE / ENVIRONMENT", "Do not claim it runs", "No push", "check setup/entrypoint/tests if Build"):
            self.assertIn(phrase, text)

    def test_references_are_present(self):
        text = self.read(SKILL / "SKILL.md")
        for p in ("project-assessment.md", "first-run-safety.md"):
            self.assertIn(p, text)
            self.assertTrue((SKILL / "references" / p).is_file())

    def test_new_skill_does_not_embed_foreign_project_specific_data(self):
        text = "\n".join(self.read(p) for p in SKILL.rglob("*.md"))
        for forbidden in ("timeline-tool", "4ort.bayern", "sergei@", "D:\\Projects\\", "github.com/SergejDAGDA/"):
            self.assertNotIn(forbidden, text)

    def test_prepare_memory_gate_is_mandatory_before_commit(self):
        skill = self.read(SKILL / "SKILL.md")
        safety = self.read(SKILL / "references/first-run-safety.md")
        for name in ("PROJECT.md", "STATUS.md", "DECISIONS.md", "SESSION_LOG.md", "HANDOFF.md"):
            self.assertIn(name, skill)
        for marker in (
            "Project memory protocol: maintain-project-memory/v2",
            "Project memory schema: project-memory/v1",
            "Canonical project-memory root: docs/project-memory",
            "Memory update policy",
            "Local Git commit policy",
            "audit_project_memory.py <project-root>",
        ):
            self.assertIn(marker, skill)
        self.assertIn("before staging", skill)
        self.assertIn("BLOCKER / INCOMPLETE", skill)
        self.assertIn("a **BLOCKER**", safety)
        gate = skill.split("6. **Verify and checkpoint (mode-aware completion gate).**", 1)[1].split("\n7. **Make a scoped local commit", 1)[0]
        self.assertIn("**Before staging or claiming a successful Bootstrap**", gate)
        self.assertIn("**Integrated memory gate (owner installed):**", gate)
        self.assertIn("**Standalone memory gate (owner absent):**", gate)
        self.assertIn("audit_project_memory.py <project-root>", gate)
        self.assertIn("**BLOCKER / INCOMPLETE**", gate)


    def assert_adoption_completion_contract(self, skill: str):
        """The two routing checks belong to the integrated completion gate itself."""
        gate = skill.split("6. **Verify and checkpoint (mode-aware completion gate).**", 1)[1].split(
            "\n7. **Make a scoped local commit", 1
        )[0]
        memory = gate.split("**Integrated memory gate (owner installed):**", 1)[1].split(
            "\n   - **Standalone memory gate", 1
        )[0]
        for required in (
            "audit_project_memory.py <project-root> --adoption",
            "ADOPTION wip_continuity_routing=declared",
            "ADOPTION checkpoint_routing=declared",
            "process exit code",
            "adoption audit may exit `0`",
            "**BLOCKER / INCOMPLETE**",
        ):
            self.assertIn(required, memory)
        return memory

    def test_integrated_bootstrap_adoption_gate_rejects_warning_success(self):
        original = self.read(SKILL / "SKILL.md")
        self.assert_adoption_completion_contract(original)
        # Negative mutations must fail even if the text remains elsewhere in SKILL.md.
        for before, after in (
            ("audit_project_memory.py <project-root> --adoption", "audit_project_memory.py <project-root>"),
            ("ADOPTION wip_continuity_routing=declared", "wip routing checked"),
            ("ADOPTION checkpoint_routing=declared", "checkpoint routing checked"),
            ("adoption audit may exit `0`", "adoption audit must exit nonzero"),
        ):
            self.assertIn(before, original)
            mutated = original.replace(before, after, 1)
            with self.subTest(removed=before), self.assertRaises(AssertionError):
                self.assert_adoption_completion_contract(mutated)

    def test_plain_prompt_and_routing_regression_are_documented(self):
        readme_ru = self.read(ROOT / "README.ru.md")
        readme_en = self.read(ROOT / "README.md")
        routing = self.read(DOCS / "OPTIONAL_GLOBAL_ROUTING.md")
        acceptance = self.read(DOCS / "ACCEPTANCE.md")
        self.assertIn("<ПУТЬ_К_ПАПКЕ_ПРОЕКТА>", readme_ru)
        self.assertIn("<PROJECT_FOLDER_PATH>", readme_en)
        self.assertNotIn("timeline-tool", readme_ru.lower())
        self.assertIn("without naming any skill", acceptance)
        self.assertIn("BEFORE separately choosing", routing)
        self.assertIn("user-reviewed", routing)

    def test_report_must_distinguish_actually_applied_from_discovered_skills(self):
        skill = self.read(SKILL / "SKILL.md")
        self.assertIn("discovered/read from applied", skill)
        self.assertIn("NOT VERIFIED", skill)


    def test_identity_preflight_requires_both_roles(self):
        skill = self.read(SKILL / "SKILL.md")
        safety = self.read(SKILL / "references/first-run-safety.md")
        part = skill.split("## Early Git author/committer identity preflight", 1)[1].split("\n## Execute by ownership", 1)[0]
        for term in ("GitHub, GitLab and remotes", "author **and** committer", "user.useConfigOnly=true",
                     "one direct intermediate question", "globally", "without explicit permission"):
            self.assertIn(term, part)
        self.assertLess(skill.index("## Early Git author/committer identity preflight"),
                        skill.index("## Execute by ownership"))
        self.assertIn("not** login authorization", safety)

    def test_absent_companions_are_distinct_from_broken_companions(self):
        skill = self.read(SKILL / "SKILL.md")
        memory = skill.split("3. **Establish durable project context.**", 1)[1].split("\n4. **Create product documentation.", 1)[0]
        docs = skill.split("4. **Create product documentation.**", 1)[1].split("\n5. **Create technical foundation", 1)[0]
        for phrase in ("**not installed**", "docs/project-notes/", "do not copy",
                       "do not silently downgrade"):
            self.assertIn(phrase, memory)
        for phrase in ("If absent", "README.md", "docs/ARCHITECTURE.md", "is installed but fails"):
            self.assertIn(phrase, docs)
        self.assertIn("**BLOCKER / INCOMPLETE**", docs)

    def test_existing_files_are_classified_before_staging(self):
        skill = self.read(SKILL / "SKILL.md")
        safety = self.read(SKILL / "references/first-run-safety.md")
        part = skill.split("1. **Inspect and classify.**", 1)[1].split("\n2. **Establish local Git.", 1)[0]
        for phrase in ("actual application code, substantive configuration or maintained project-local rules", "large/binary/licensed",
                       "unrelated/unknown/sensitive", "pre-write checksums", "No indiscriminate staging"):
            self.assertIn(phrase, part)
        self.assertIn("File presence does not equal permission", safety)
        self.assertIn("global Git user identity **without explicit consent**", safety)

    def test_starter_prompts_are_plain_language(self):
        for name, placeholder, heading in (
            ("README.md", "<PROJECT_FOLDER_PATH>", "## Start a new project"),
            ("README.ru.md", "<ПУТЬ_К_ПАПКЕ_ПРОЕКТА>", "## Старт нового проекта"),
        ):
            doc = self.read(ROOT / name)
            fence = chr(96) * 3
            block = doc.split(heading, 1)[1].split(fence + "text", 1)[1].split(fence, 1)[0]
            self.assertIn(placeholder, block)
            for forbidden in ("bootstrap-software-project", "maintain-project-memory", "project-documentation",
                              "reference project", "проект-референс"):
                self.assertNotIn(forbidden, block.lower())

    def test_portability_acceptance_scenarios_exist(self):
        acceptance = self.read(DOCS / "ACCEPTANCE.md")
        for term in ("No GitHub/no author identity", "Existing identity",
                     "No companion skills", "Installed owner failure", "Existing-file matrix"):
            self.assertIn(term, acceptance)
        self.assertIn("Automatic skill discovery cannot be validated", acceptance)
        self.assertIn("without treating absence itself as an environment failure", acceptance)
        metadata = self.read(SKILL / "agents/openai.yaml")
        self.assert_metadata_is_entrypoint_only(metadata)


    def test_installable_payload_has_no_literal_personal_email(self):
        import re
        payload = "\n".join(self.read(p) for p in SKILL.rglob("*") if p.is_file())
        # Generic examples without a dot (e.g. username@hostname) are permitted.
        addresses = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", payload)
        self.assertEqual(addresses, [], "Do not distribute user identities in the portable skill")


    def assert_routing_contract(self, skill_text: str):
        """Scope semantic assertions to the authoritative route, not stray mentions."""
        route = skill_text.split("## Route the request\n\n", 1)[1].split("\n## Establish input", 1)[0]
        eligibility = route.split("**Single project-root eligibility rule:**", 1)[1].split("\n1. **Explore only:**", 1)[0]
        prepare = route.split("2. **Prepare:**", 1)[1].split("\n3. **Build:**", 1)[0]
        existing = route.split("4. **Existing project:**", 1)[1].split("\n\nThe user's explicit", 1)[0]
        self.assertIn("empty or concept-only folder", eligibility)
        self.assertIn("project-local `AGENTS.md` with maintained project rules", eligibility)
        self.assertIn("substantive configuration", eligibility)
        self.assertIn("when an owner skill is installed and usable", prepare)
        self.assertIn("when absent and not explicitly required", prepare)
        self.assertIn("An installed but failing owner is a blocker", prepare)
        self.assertNotIn("produce the approved baseline, canonical memory and product knowledge", prepare)
        self.assertIn("project-local `AGENTS.md`/maintained project rules", existing)
        self.assertIn("substantive configuration", existing)
        self.assertIn("existing-project adoption/update", existing)
        self.assertIn("Never re-bootstrap", existing)
        return route

    def test_authoritative_routing_and_owner_modes_agree(self):
        skill_text = self.read(SKILL / "SKILL.md")
        self.assert_routing_contract(skill_text)
        safety = self.read(SKILL / "references/first-run-safety.md")
        self.assertIn("single project-root eligibility rule", safety)
        completion = skill_text.split("## Completion states", 1)[1].split("\n## Final report", 1)[0]
        for phrase in ("Evaluate memory and product-documentation owners **independently**",
                       "installed-but-failing", "explicitly required-but-absent", "**mixed**"):
            self.assertIn(phrase, completion)

    def test_routing_negative_mutations_cannot_pass_from_other_sections(self):
        original = self.read(SKILL / "SKILL.md")
        self.assert_routing_contract(original)
        eligibility_key = "project-local `AGENTS.md` with maintained project rules"
        existing_key = "project-local `AGENTS.md`/maintained project rules"
        prepare_key = "when absent and not explicitly required"
        for before, after in (
            (eligibility_key, "user-supplied design input"),
            (existing_key, "generic documentation"),
            (prepare_key, "always requiring canonical documents"),
        ):
            self.assertIn(before, original)
            mutated = original.replace(before, after, 1)
            with self.subTest(removed=before), self.assertRaises(AssertionError):
                self.assert_routing_contract(mutated)


    def assert_metadata_is_entrypoint_only(self, metadata: str):
        """Installable metadata cannot independently define fallback policy."""
        self.assertIn('default_prompt: "', metadata)
        prompt = metadata.split('default_prompt: "', 1)[1].split('"', 1)[0]
        self.assertIn("Use $bootstrap-software-project", prompt)
        self.assertIn("Follow SKILL.md as the sole workflow contract", prompt)
        self.assertNotRegex(
            prompt.lower(),
            r"\b(if|else|otherwise|fallback|standalone|installed|absent|unavailable|incompatible|write-eligible)\b",
        )
        self.assertNotIn("maintain-project-memory", prompt)
        self.assertNotIn("project-documentation", prompt)

    def test_installable_metadata_cannot_define_owner_fallback(self):
        metadata = self.read(SKILL / "agents/openai.yaml")
        self.assert_metadata_is_entrypoint_only(metadata)
        for competing in (
            " otherwise use standalone",
            " if installed and usable",
            " fallback when incompatible",
        ):
            mutated = metadata.replace(
                "Follow SKILL.md as the sole workflow contract",
                "Follow SKILL.md as the sole workflow contract" + competing,
                1,
            )
            with self.subTest(competing=competing), self.assertRaises(AssertionError):
                self.assert_metadata_is_entrypoint_only(mutated)

    def test_contract_ownership_is_declared_and_safety_defers(self):
        skill_text = self.read(SKILL / "SKILL.md")
        safety_text = self.read(SKILL / "references/first-run-safety.md")
        self.assertIn("**Contract authority:**", skill_text)
        authority = skill_text.split("**Contract authority:**", 1)[1].split("\n## Route the request", 1)[0]
        self.assertIn("sole normative source", authority)
        self.assertIn("agents/openai.yaml", authority)
        self.assertIn("does not define who is installed, when fallback is allowed", safety_text)
        self.assertNotIn("**Integrated release gate:**", safety_text)
        self.assertNotIn("**Standalone release gate:**", safety_text)

    def test_markdown_hygiene(self):
        paths = list(ROOT.rglob("*.md"))
        self.assertGreaterEqual(len(paths), 6)
        for path in paths:
            data = path.read_bytes()
            self.assertTrue(data.endswith(b"\n"), str(path))
            self.assertFalse(data.endswith(b"\n\n"), str(path))
            for line in data.splitlines():
                self.assertFalse(line.endswith((b" ", b"\t")), str(path))


if __name__ == "__main__":
    unittest.main()
