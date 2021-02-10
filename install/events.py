from soulstruct.bloodborne.events import convert_events


def main():
    convert_events("emevd.dcx", "../package/event", input_type="evs.py", input_directory="../events")


if __name__ == '__main__':
    main()
