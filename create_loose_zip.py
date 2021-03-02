import zipfile
from pathlib import Path


def main():
    with zipfile.ZipFile("BloodborneBossRush_Loose.zip", mode="w", compression=zipfile.ZIP_DEFLATED) as z:
        for game_file in Path("package").rglob("*"):
            if game_file.name.endswith(".dcx"):
                arcname = game_file.relative_to("package")
                z.write(game_file, arcname)


if __name__ == '__main__':
    main()
