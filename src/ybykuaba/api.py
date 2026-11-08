import subprocess
import sys

import webview

from ybykuaba import database


class YbykuabaAPI:
    """API de comunicação entre Python e JavaScript"""

    def __init__(self):
        pass

    def close(self):
        webview.windows[0].destroy()
        sys.exit()

    def find_app(self, query: str): ...

    def find_archive(self, query: str):
        result = database.find_archive(query)
        return result

    def calculate(self, query: str): ...

    def execute(self, query: str): ...

    def open_path(self, path):
        try:
            subprocess.Popen(["xdg-open", path])
        except:
            subprocess.Popen(["gio", "open", path])
