import sqlite3
from pathlib import Path

from platformdirs import user_data_path

from ybykuaba.core import apps, archives

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
                name TEXT NOT NULL,
                bin TEXT NOT NULL
            );
        """)


def sync():
    """Sinconiza os aplicativos e arquivos novos com o banco de dados"""
    new_files_index: list[str] = archives.get_index(archives.STANDARD_PATHS)
    new_apps_index: list[tuple] = apps.get_index()

    with sqlite3.connect(DB_PATH) as db:
        # deleta tudo de arquivos
        db.execute("DELETE FROM files")
        # adiciona todos os arquivos
        db.executemany(
            "INSERT INTO files (path, name) VALUES (?, ?)",
            [(path, Path(path).name) for path in new_files_index],
        )
        # delata tudo dos apps
        db.execute("DELETE FROM applications")
        # adiciona tudo novamente
        db.executemany(
            "INSERT INTO applications (name, bin) VALUES (?, ?)", new_apps_index
        )


def find_archive(query: str, limit: int = 5) -> list[str]:
    """busca arquivos e pastas dentro do banco de dados"""
    with sqlite3.connect(DB_PATH) as db:
        rows = db.execute(
            """
            SELECT path FROM files
            WHERE name LIKE ?
            ORDER BY length(name)
            LIMIT ?
            """,
            (f"%{query}%", limit),
        ).fetchall()

    return [row[0] for row in rows]


def find_application(query: str, limit: int = 5) -> list[tuple[str, str]]:
    """busca aplicativos dentro do banco de dados"""
    with sqlite3.connect(DB_PATH) as db:
        rows = db.execute(
            """
            SELECT name, bin FROM applications
            WHERE name LIKE ?
            ORDER BY length(name)
            LIMIT ?
            """,
            (f"%{query}%", limit),
        ).fetchall()
    return rows
