import os
from pathlib import Path

from soulstruct.bloodborne.events import convert_events


def main():
    convert_events("emevd.dcx", "../package/event", input_type="evs.py", input_directory="../events")
    for bak_file in Path("../package/event").glob("*.bak"):
        os.remove(bak_file)


if __name__ == '__main__':
    main()
