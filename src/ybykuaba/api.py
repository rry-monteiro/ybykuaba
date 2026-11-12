import subprocess
import sys
from pathlib import Path

import webview

from ybykuaba import database

from .core import calc, commands, web


class YbykuabaAPI:
    """API de comunicação entre Python e JavaScript"""

    def __init__(self):
        pass

    def close(self) -> None:
        """Destrói a janela doo app e fecha o programa"""
        webview.windows[0].destroy()
        sys.exit()

    def find_app(self, query: str) -> list[dict[str, str]]:
        """
        recebe o nome do app e manda pro banco de dados, que retorna uma lista de tuplas
        (name, bin), ajusta essa lista de tulas numa llista de dicionários e retorna
        """
        db_res: list[tuple[str, str]] = database.find_application(query)
        return [{"name": name, "bin": bin_} for name, bin_ in db_res]

    def find_archive(self, query: str) -> list[dict[str, str | bool]]:
        """
        Recebe a busca e manda ela pro banco de dados, recebe uma lista de tuplas de volta
        transforma a lista de tuplas numa lista de dicionários contendo {"name":"", "path":"", "id_dir":bool}
        assim o js sabe que tipo de ícone mostrar
        """
        db_res: list[str] = database.find_archive(query)
        return [
            {"name": Path(r).name, "path": r, "is_dir": Path(r).is_dir()}
            for r in db_res
        ]

    def search_web(self, query:str)->None:
        """
        envia a pesquisa pra search e abre o navegador, não retorna nada
        """
        web.search(query)

    def calculate(self, query: str) -> dict[str, str | bool]:
        """
        Recebe a query da expressão e envia pra calculadora, retorna o resultado do pysym
        em um dict { "resultado" : "...", "sucesso": bool }
        """
        return calc.parse_expression(query)

    def execute(self, query: str) -> str:
        """
        Recebe a quero do usuário e envia pra execução, rotorna o que o programa retornar
        """
        return commands.run_command(query)

    def open_app(self, app_bin: str) -> None:
        """
        recebe o string do caminho do binário de um programa e abre com Popen
        """
        subprocess.Popen([app_bin], shell=True)

    def open_path(self, path: str) -> None:
        """
        Recebe o caminho do documento ou pasta que vai, itera em uma lista de
        possiveis programas instalados e tenta cada um, quando consegue, quebra
        """
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
