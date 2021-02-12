import shutil
from pathlib import Path


def install_to_disc():
    for file_path in Path("package").rglob("*"):
        if not file_path.is_file() or file_path.suffix == ".bak":
            continue
        relative_path = file_path.relative_to("package")
        shutil.copy2(Path("package", relative_path), Path("DISC_v1.09/Image0/dvdroot_ps4", relative_path))


if __name__ == '__main__':
    install_to_disc()
