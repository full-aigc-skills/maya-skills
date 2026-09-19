import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HostNeutralMayaSkillIdentity(unittest.TestCase):
    def test_installable_skills_have_no_legacy_plugin_identity(self) -> None:
        legacy = ("codex-dreamina-3d", "codex-maya")
        for path in sorted((ROOT / "skills").glob("**/*")):
            if not path.is_file() or path.suffix != ".md":
                continue
            text = path.read_text(encoding="utf-8")
            for value in legacy:
                self.assertNotIn(value, text, f"{path} still contains {value}")


if __name__ == "__main__":
    unittest.main()
