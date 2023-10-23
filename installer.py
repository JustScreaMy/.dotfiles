#!/usr/bin/env python3.11
import argparse
import sys
from pathlib import Path
from typing import Sequence

from config_mountpoints import mountpoints
 
DOTFILES_PATH = Path(__file__).parent
CONFIGS_PATH = DOTFILES_PATH / "configs"
USER_CONFIG_PATH = Path("~/.config").expanduser()

def _get_directory(path: str, type: str) -> Path:
    path = Path(path).expanduser()
    return path if type == "dir" else path.parent    

def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser("installer.py")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="run the cli without writing changes",
    )
    args = parser.parse_args(argv)

    to_mount = len(mountpoints)

    if not USER_CONFIG_PATH.exists():
        print(f"Directory {USER_CONFIG_PATH} doesn't exists! Creating...")
        
        if not args.dry_run:
            USER_CONFIG_PATH.mkdir()

    for count, (config, mountpoint) in enumerate(mountpoints.items(), start=1):

        managed_file_path = CONFIGS_PATH / config
        target_file_path = Path(mountpoint["path"]).expanduser()
        target_file_directory = _get_directory(target_file_path, mountpoint["type"])

        if mountpoint["type"] == "dir":
            print(f"[{count}/{to_mount}] Mounting directory '{target_file_path}'")
            # if not target_file_directory.exists():
                
            #     print(f"[{count}/{to_mount}] {target_file_directory} not exists")
            #     print(f"[{count}/{to_mount}] Creating {target_file_directory}")
                
            #     if not args.dry_run:
            #         target_file_directory.mkdir(parents=True)
            
            # elif
            if target_file_directory.is_symlink():
                
                print(f"[{count}/{to_mount}] {target_file_directory} is a symlink to {target_file_directory.readlink()}")
                print(f"[{count}/{to_mount}] Unlinking '{target_file_path}'")
                
                if not args.dry_run:
                    target_file_directory.unlink()
            
            elif target_file_directory.exists():
                print(f"[{count}/{to_mount}] {target_file_directory} exists, making backup of it")
                print(f"[{count}/{to_mount}] Renaming {target_file_directory} to {target_file_directory}.before_manage")
        
                if not args.dry_run:
                    target_file_directory.rename(f"{target_file_directory.name}.before_manage")

            print(f"[{count}/{to_mount}] Symlinking managed configuration directory to target")

            if not args.dry_run:
                target_file_directory.symlink_to(managed_file_path, target_is_directory=True)

        elif mountpoint["type"] == "file":
        
            print(f"[{count}/{to_mount}] Mounting file '{target_file_path}'")
            
            if not target_file_directory.exists():
                
                print(f"[{count}/{to_mount}] {target_file_directory} not exists")
                print(f"[{count}/{to_mount}] Creating {target_file_directory}")
                
                if not args.dry_run:
                    target_file_directory.mkdir(parents=True)

            if target_file_path.exists():

                print(f"[{count}/{to_mount}] File {target_file_path} exists, making backup of it")

                if not args.dry_run:
                    target_file_path.rename(f"{target_file_directory.name}.before_manage")
            
            print(f"[{count}/{to_mount}] Symlinking managed configuration file to target")

            if not args.dry_run:
                target_file_path.symlink_to(managed_file_path)


if __name__ == "__main__":
    raise SystemExit(main())