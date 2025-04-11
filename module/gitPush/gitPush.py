import subprocess
import json
import sys
import os
from pathlib import Path


def check_git_installed():
    """Check if Git have already installed"""
    try:
        subprocess.run(["git", "--version"],
                       check=True,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print("I: Git have already installed [", end="")
        subprocess.run(["git", "--version"])
        print("]")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("E: Can't detect Git, please install Git first or check if Git in system variables.")
        sys.exit(1)


def run_git_commands(gitFolder: str):
    """Run Git commands"""
    if not os.path.isdir(gitFolder):
        print(f"E: Invalid path  [{gitFolder}]")
        sys.exit(2)

    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", "Update"],
        ["git", "pull", "origin", "master"],
        ["git", "push", "origin", "master"]
    ]

    for cmd in commands:
        print(f"I: Running[{' '.join(cmd)}]")
        try:
            subprocess.run(cmd,
                           check=True,
                           cwd=gitFolder,
                           stdout=sys.stdout,
                           stderr=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"E: Get error [{e.returncode}]")
            sys.exit(1)


def main(gitFolder: str):
    """Main function that run commands."""
    check_git_installed()
    run_git_commands(gitFolder)


if __name__ == "__main__":
    # Load configuration
    global config
    with open('../../config.json', 'r') as c_f:
        config = json.load(c_f)
    gitFolder = Path(config["gitFolder"])
    main(gitFolder)
