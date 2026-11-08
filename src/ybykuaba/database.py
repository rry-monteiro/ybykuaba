import sqlite3
from pathlib import Path

from platformdirs import user_data_path

from ybykuaba.core import archives

(DB_DIR := user_data_path("ybykuaba")).mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / "index.db"


def initialize():
    """cria as tabelas de aplicativos e tabelas de arquivos/pastas"""
    with sqlite3.connect(DB_PATH) as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                path TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY,
                path TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL
            );
        """)


def sync():
    """Sinconiza os aplicativos e arquivos novos com o banco de dados"""
    new_files_index: list[str] = archives.get_index(archives.STANDARD_PATHS)
    # new_apps:list[str] = apps.get_index(...)

    with sqlite3.connect(DB_PATH) as db:
        # deleta tudo de arquivos
        db.execute("DELETE FROM files")
        # adiciona todos os arquivos
        db.executemany(
            "INSERT INTO files (path, name) VALUES (?, ?)",
            [(path, Path(path).name) for path in new_files_index],
        )

