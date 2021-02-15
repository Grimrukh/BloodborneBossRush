from soulstruct import BB_PATH
from soulstruct.bloodborne.events import EMEVD


def write_numeric():
    vanilla = EMEVD(BB_PATH + "/event/m24_01_00_00.emevd.dcx")
    boss_rush = EMEVD("events/m24_01_00_00.evs.py")
    vanilla.write_numeric("central_yharnam_vanilla.txt")
    boss_rush.write_numeric("central_yharnam_boss_rush.txt")


if __name__ == '__main__':
    write_numeric()
