import sys

import webview


class YbykuabaAPI:
    """API de comunicação entre Python e JavaScript"""

    def __init__(self):
        pass

    def close(self):
        webview.windows[0].destroy()
        sys.exit()

    def find_app(self, query: str): ...

    def find_archive(self, query: str): ...

    def calculate(self, query: str): ...

    def execute(self, query: str): ...
