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
        self.assertRegex(text, r"(?m)^description: .*substantial NEW software project")
        self.assertIn("Not for brainstorming alone", text)
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
        self.assertEqual(self.read(SKILL / "VERSION").strip(), "0.1.0")

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
        self.assertIn("do not claim full completion", text)
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

    def test_verification_and_completion_are_not_faked(self):
        text = self.read(SKILL / "SKILL.md")
        for phrase in ("PREPARED", "BUILD READY", "INCOMPLETE / ENVIRONMENT", "Do not claim it runs", "No push", "actual tests"):
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
