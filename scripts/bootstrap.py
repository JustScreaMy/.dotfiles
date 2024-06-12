#!/usr/bin/env python3.12
import subprocess as sp
import sys
import tempfile
import urllib.request
from pathlib import Path

VIRTUALENV_PYZ = "https://bootstrap.pypa.io/virtualenv.pyz"
PIPX_LOCAL_DIR = Path("~/.local/opt/venv").expanduser()
LOCAL_BIN_DIR = Path("~/.local/bin").expanduser()


def get_virtualenv_pyz(dir_path: Path) -> Path:
    print("Getting virtualenv.pyz")
    urllib.request.urlretrieve(VIRTUALENV_PYZ, dir_path / "virtualenv.pyz")
    print("Finished")
    return dir_path / "virtualenv.pyz"


def init_pipx(venv_pyz_path: Path) -> tuple[Path, Path]:
    print("Initializing pipx")
    sp.check_output(
        [sys.executable, venv_pyz_path, PIPX_LOCAL_DIR],
        stderr=sp.STDOUT,
    )

    sp.check_output(
        [
            Path(PIPX_LOCAL_DIR) / "bin" / "pip",
            "install", "pipx", "virtualenv",
        ],
        stderr=sp.STDOUT,
    )

    return (
        Path(PIPX_LOCAL_DIR) / "bin" / "pipx",
        Path(PIPX_LOCAL_DIR) / "bin" / "virtualenv",
    )


def symlink_executables(executables: list[Path]):
    if not LOCAL_BIN_DIR.exists():
        print(f"Creating {LOCAL_BIN_DIR}")
        LOCAL_BIN_DIR.mkdir()
    for executable in executables:
        print(f"Symlinking {executable} -> {LOCAL_BIN_DIR}")
        (LOCAL_BIN_DIR / executable.name).symlink_to(executable)


def main() -> int:
    with tempfile.TemporaryDirectory() as dirname:
        print(f"Created tmpdir -> {dirname}")
        virtualenv_pyz_path = get_virtualenv_pyz(Path(dirname))
        print(f"Installed temporary virtualenv.pyz to {virtualenv_pyz_path}")
        pipx_path, virtualenv_path = init_pipx(virtualenv_pyz_path)
    print("Symlinking executables")
    symlink_executables([pipx_path, virtualenv_path])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
