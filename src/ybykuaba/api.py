import subprocess
import sys
from pathlib import Path

import webview

from ybykuaba import database

from .core import calc, commands


class YbykuabaAPI:
    """API de comunicação entre Python e JavaScript"""

    def __init__(self):
        pass

    def close(self):
        webview.windows[0].destroy()
        sys.exit()

    def find_app(self, query: str):
        db_res = database.find_application(query)
        res = []
        for r in db_res:
            res.append({"name": r[0], "bin": r[1]})
        return res

    def find_archive(self, query: str) -> list[dict[str, str | bool]]:
        db_res = database.find_archive(query)
        res = []
        for r in db_res:
            path = Path(r)
            res.append({"name": path.name, "path": r, "is_dir": path.is_dir()})
        return res

    def calculate(self, query: str):
        res = calc.parse_expression(query)
        return res

    def execute(self, query: str):
        res = commands.run_command(query)
        print(res)
        return res

    def open_app(self, app_bin):
        subprocess.Popen([app_bin], shell=True)

    def open_path(self, path):
        open_commands = [
            ["xdg-open", path],
            ["gio", "open", path],
            ["gnome-open", path],
            ["kde-open", path],
        ]

        for cmd in open_commands:
            try:
                subprocess.Popen(cmd)
                break  # se executou com sucesso, interrompe o loop
            except FileNotFoundError:
                continue
