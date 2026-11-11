import shlex
from pathlib import Path

from xdg.BaseDirectory import xdg_data_dirs
from xdg.DesktopEntry import DesktopEntry


def _get_desktop_files():
    apps = []
    for directory in xdg_data_dirs:
        applications = Path(directory) / "applications"
        if applications.is_dir():
            apps.extend(
                DesktopEntry(str(path)) for path in applications.rglob("*.desktop")
            )
    return apps


def get_index():
    index = []
    desktop_entrys = _get_desktop_files()
    for app in desktop_entrys:
        appbin = shlex.split(str(app.getExec()))[0]
        index.append((app.getName(),  appbin))
    return index
