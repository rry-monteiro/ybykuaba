from pathlib import Path

import webview

from ybykuaba.api import YbykuabaAPI

UI = Path(__file__).parent / "ui" / "index.html"
API = YbykuabaAPI()

def main():
    webview.create_window(
        title="ybykûaba",
        url=str(UI),
        zoomable=False,
        frameless=True,
        resizable=False,
        min_size=(400, 400),
        width=400,
        height=400,
        js_api=API,
    )
    webview.start(gui="qt")


if __name__ == "__main__":
    main()
