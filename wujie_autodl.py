"""Wujie AutoDL companion entry point. Standard library only."""
import argparse
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys

REPOSITORY = "https://github.com/z4568114-crypto/wujie-autodl"
DEFAULT_ROOT = Path("/root/wujie-image")
MARKER = "wujie-autodl-art-environment-v1"


def inspect_environment(root, include_models=True):
    root = Path(root).expanduser().resolve()
    checks = []
    marker = root / ".wujie-image"
    try:
        with marker.open("r", encoding="utf-8") as stream:
            marker_ok = stream.read(256).strip() == MARKER
    except (OSError, UnicodeError):
        marker_ok = False
    checks.append({"name": "environment-marker", "path": str(marker), "present": marker_ok})
    for relative in ("start.py", "ComfyUI/main.py", "ComfyUI/.venv/bin/python"):
        path = root / relative
        checks.append({"name": relative, "path": str(path), "present": path.is_file()})
    if include_models:
        manifest = Path(__file__).with_name("model-sources.json")
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))["models"]
            seen = set()
            for item in entries:
                if not item.get("requiredInPreparedEnvironment", False):
                    continue
                raw = item.get("installedPath")
                if not raw or raw in seen:
                    continue
                relative = PurePosixPath(raw).relative_to(PurePosixPath(str(DEFAULT_ROOT)))
                if ".." in relative.parts:
                    raise ValueError("invalid model path")
                seen.add(raw)
                path = root.joinpath(*relative.parts)
                checks.append({"name": item["id"], "path": str(path), "present": path.is_file()})
            if not seen:
                raise ValueError("empty model list")
        except (OSError, ValueError, KeyError, TypeError) as error:
            checks.append({"name": "model-manifest", "present": False,
                           "error": type(error).__name__})
    present = sum(bool(item["present"]) for item in checks)
    return {"repository": REPOSITORY, "root": str(root),
            "scope": "file-presence-only; no hash verification or inference",
            "status": "files-present" if present == len(checks) else "missing-files",
            "present": present, "total": len(checks), "checks": checks}


def main(argv=None):
    parser = argparse.ArgumentParser(description="无界 AutoDL 配套镜像入口")
    parser.add_argument("command", choices=("about", "check", "start"))
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                        help="已有配套环境目录，默认 /root/wujie-image")
    args = parser.parse_args(argv)
    if args.command == "about":
        print(json.dumps({"name": "wujie-autodl", "repository": REPOSITORY,
                          "status": "publication-preparation",
                          "purpose": "Environment inspection and existing-image startup",
                          "downloadsModels": False}, ensure_ascii=False, indent=2))
        return 0
    report = inspect_environment(args.root, include_models=args.command == "check")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    if report["status"] != "files-present":
        return 1
    if args.command == "check":
        return 0
    root = Path(report["root"])
    try:
        return subprocess.call([sys.executable, str(root / "start.py")], cwd=str(root))
    except KeyboardInterrupt:
        return 130
    except OSError as error:
        print(json.dumps({"status": "launch-failed", "error": type(error).__name__}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
