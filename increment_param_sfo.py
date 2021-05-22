from pathlib import Path

APP_VER_OFFSET = 0x353


def update(force_value: int = None):
    sfo_path = Path("DISC_v1.09/Image0/sce_sys/param.sfo")
    with sfo_path.open("rb") as f:
        sfo = f.read()

    current_app_ver = int(sfo[APP_VER_OFFSET:APP_VER_OFFSET + 2])

    if force_value is not None:
        msg = f"Current `param.sfo` app version is {current_app_ver}. Change to {force_value}? [y/n]"
    else:
        msg = f"Current `param.sfo` app version is {current_app_ver}. Increment? [y/n]"

    if input(msg).lower() == "y":
        if force_value:
            new_app_ver = int(force_value)
        else:
            new_app_ver = current_app_ver + 1
        sfo = sfo[:APP_VER_OFFSET] + str(new_app_ver).encode(encoding="ascii") + sfo[APP_VER_OFFSET + 2:]
        with sfo_path.open("wb") as f:
            f.write(sfo)
        print(f"Updated `param.sfo` app version: 01.{current_app_ver} -> 01.{new_app_ver}")
    else:
        print("Exiting.")


if __name__ == '__main__':
    update(12)
