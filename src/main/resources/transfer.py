import shutil
from pathlib import Path


def transfer_lib_contents():
    project_root = Path(__file__).resolve().parents[3]
    source_dir = project_root / "src" / "main" / "resources" / "lib"
    target_dir = project_root / "run" / "plugins" / "PySoup" / "scripts"

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    target_dir.mkdir(parents=True, exist_ok=True)

    for item in source_dir.iterdir():
        destination = target_dir / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)


if __name__ == "__main__":
    transfer_lib_contents()

