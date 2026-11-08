from pathlib import Path

from xdg.BaseDirectory import xdg_data_dirs


def get_desktop_files():
    apps = []
    for directory in xdg_data_dirs:
        applications = Path(directory) / "applications"

        if applications.is_dir():
            apps.extend(applications.rglob("*.desktop"))
    return apps


def get_data_desktop(apps: list): ...
