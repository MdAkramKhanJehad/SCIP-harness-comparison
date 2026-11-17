"""Integration checks with a third harness, without importing either product."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

PSEUDO = Path(__file__).resolve().parents[2]


class HarnessCatalogTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.pseudo = self.root / "pseudocode"
        (self.pseudo / "tools/worklists").mkdir(parents=True)
        shutil.copytree(PSEUDO / "schema", self.pseudo / "schema")
        for name in ("harnesses.py", "pseudo_parse.py", "check_pseudocode.py", "check_src.py",
                     "check_coverage.py", "build_knobspace.py", "class_name.py"):
            shutil.copyfile(PSEUDO / "tools" / name, self.pseudo / "tools" / name)
        source = self.root / "source"
        source.mkdir()
        (source / "runner.py").write_text("def run():\n    return 3\n")
        catalog = [dict(key="sample", folder="sample", name="Sample", repo="../source",
                        registry="sample.yaml", out="sample.knobs.json", version=None, profiles=None,
                        worklist_tokens=["sample"], source_globs=["*.py"])]
        (self.pseudo / "harnesses.json").write_text(json.dumps(catalog))
        knob = dict(id="scan.limit", origin="code_constant", kind="implicit", type="int", default=3,
                    source="runner.py:2", does="Caps work", affects=["cost"])
        registry = dict(commit="abc", about="Test-only harness", categories={"budget_and_termination": {"limits": [knob]}})
        (self.root / "sample.yaml").write_text(yaml.safe_dump(registry))
        (self.pseudo / "tools/worklists/sample_core.json").write_text(json.dumps([dict(id="scan.limit", target="runner.pseudo")]))
        (self.pseudo / "sample").mkdir()
        self.file = self.pseudo / "sample/runner.pseudo"
        self.file.write_text('// file: runner.py\n@executedBy(CODE) @role(pipeline)\nclass Sample {\n'
                             '    @src("runner.py:1")\n    int run(Theta θ) {\n'
                             '        return θ["scan.limit"]; // src: runner.py:2\n    }\n}\n')

    def tool(self, name, *args):
        return subprocess.run([sys.executable, str(self.pseudo / "tools" / name), *args],
                              cwd=self.root.parent, text=True, capture_output=True)

    def test_new_harness_uses_shared_tools_without_code_changes(self):
        for tool, args in [("check_pseudocode.py", ("--harness", "sample", "--calls", "--strict")),
                           ("check_src.py", ()), ("check_coverage.py", ()), ("build_knobspace.py", ())]:
            with self.subTest(tool=tool):
                result = self.tool(tool, *args)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        doc = json.loads((self.pseudo / "sample/sample.knobs.json").read_text())
        self.assertEqual(doc["harness"]["name"], "Sample")
        self.assertEqual(doc["knobs"][0]["component"], "runner.pseudo#Sample.run")

    def test_bad_annotation_fails_from_an_unrelated_working_directory(self):
        self.file.write_text(self.file.read_text().replace('runner.py:1', 'runner.py:999'))
        result = self.tool("check_src.py")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("line out of range runner.py", result.stdout)

    def test_strict_mode_rejects_unresolved_known_class_calls(self):
        self.file.write_text(self.file.read_text().replace('return θ', 'Sample.missing(); return θ'))
        result = self.tool("check_pseudocode.py", "--strict", "--calls")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Sample.missing", result.stdout)

    def test_shared_relative_paths_require_an_explicit_naming_table(self):
        tables = {"one": {"src/runner.pseudo": "First"}, "two": {"src/runner.pseudo": "Second"}}
        (self.pseudo / "tools/class_names.json").write_text(json.dumps(tables))
        result = self.tool("class_name.py", "--harness", "two", "src/runner.pseudo")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Second")
        result = self.tool("class_name.py", "src/runner.pseudo")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ambiguous class name", result.stderr)


if __name__ == "__main__":
    unittest.main()
