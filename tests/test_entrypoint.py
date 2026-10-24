import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / "wujie_autodl.py"
spec = importlib.util.spec_from_file_location("wujie_autodl", MODULE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class EntrypointTests(unittest.TestCase):
    def test_about_does_not_require_cloud_or_execute_commands(self):
        output = io.StringIO()
        with patch.object(app.subprocess, "call") as call, contextlib.redirect_stdout(output):
            self.assertEqual(app.main(["about"]), 0)
        self.assertFalse(json.loads(output.getvalue())["downloadsModels"])
        call.assert_not_called()

    def test_missing_environment_cannot_launch(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(app.subprocess, "call") as call, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(app.main(["start", "--root", directory]), 1)
            call.assert_not_called()

    def test_wrong_marker_rejected_and_model_mounts_reported_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".wujie-image").write_text("unrelated-environment")
            report = app.inspect_environment(root)
            self.assertEqual(report["status"], "missing-files")
            self.assertFalse(report["checks"][0]["present"])
            self.assertGreater(report["total"], 4)

    def test_valid_existing_environment_delegates_to_its_launcher(self):
        with tempfile.TemporaryDirectory(prefix="wujie test ") as directory:
            root = Path(directory).resolve()
            (root / ".wujie-image").write_text(app.MARKER + "\n")
            for relative in ("start.py", "ComfyUI/main.py", "ComfyUI/.venv/bin/python"):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("")
            with patch.object(app.subprocess, "call", return_value=7) as call, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(app.main(["start", "--root", str(root)]), 7)
            call.assert_called_once_with([app.sys.executable, str(root / "start.py")], cwd=str(root))
            self.assertEqual(app.inspect_environment(root)["status"], "missing-files")


if __name__ == "__main__":
    unittest.main()
