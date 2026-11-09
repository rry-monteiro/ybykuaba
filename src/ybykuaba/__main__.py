import threading
from pathlib import Path

import webview

from ybykuaba import database
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
        on_top=True,
        width=400,
        height=400,
        js_api=API,
    )
    webview.start(gui="qt")
    # inicializa o banco de dados
    database.initialize()
    # faz a sincronização
    threading.Thread(target=database.sync(), daemon=True).start()


if __name__ == "__main__":
    main()
