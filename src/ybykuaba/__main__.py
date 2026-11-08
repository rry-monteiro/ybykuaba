from pathlib import Path

import webview

UI = (Path(__file__).parent / "ui" / "index.html")

def main():
    webview.create_window(title="ybykûaba", url=str(UI))
    webview.start(gui="qt")


if __name__ == "__main__":
    main()
