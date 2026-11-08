import sqlite3

from platformdirs import user_data_path

(DB_DIR := user_data_path("ybykuaba")).mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / "index.db"

db = sqlite3.connect(DB_PATH)

def initialize():
    # cria as tabelas de aplicativos e tabelas de arquivos/pastas
    db.executescript("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL UNIQUE
        );
    """)
    db.commit()


