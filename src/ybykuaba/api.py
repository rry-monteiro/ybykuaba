import subprocess
import sys
from pathlib import Path

import webview

from ybykuaba import database


class YbykuabaAPI:
    """API de comunicação entre Python e JavaScript"""

    def __init__(self):
        pass

    def close(self):
        webview.windows[0].destroy()
        sys.exit()

    def find_app(self, query: str):
        result = database.find_application(query)
        return result

    def find_archive(self, query: str)->list[dict[str,str|bool]]:
        db_res = database.find_archive(query)
        res = []
        for r in db_res:
            path = Path(r)
            res.append({
                "name": path.name,
                "path": r,
                "is_dir": path.is_dir()
            })
        return res

    def calculate(self, query: str): ...

    def execute(self, query: str): ...

    def open_path(self, path):
        commands = [
                ["xdg-open", path],
                ["gio", "open", path],
                ["gnome-open", path],
                ["kde-open", path]
            ]
            
        for cmd in commands:
            try:
                subprocess.Popen(cmd)
                break  # se executou com sucesso, interrompe o loop
            except FileNotFoundError:
                continue


