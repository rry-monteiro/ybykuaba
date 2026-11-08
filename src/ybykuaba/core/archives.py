from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import platformdirs as pt

# lista de nomes de diretórios a serem ignorados
IGNORE_DIRS: set[str] = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    ".cache",
    "site-packages",
}

# lista de extensões para serem ignoradas (aplicativos)
IGNORE_EXTENSIONS: set[str] = {
    ".desktop",
    ".appimage",
    ".flatpakref",
    ".flatpakrepo"
}

# lista de pastas padrão a serem varridas
STANDARD_PATHS: set[Path] = {
    pt.user_desktop_path(),
    pt.user_downloads_path(),
    pt.user_documents_path(),
    pt.user_projects_path(),
    pt.user_music_path(),
    pt.user_pictures_path(),
}


def _scan_dir(path: Path) -> list[str]:
    paths = []
    for root, directories, files in path.walk():
        directories[:] = [
            directory for directory in directories if directory not in IGNORE_DIRS
        ]
        paths.extend(str(root / directory) for directory in directories)
        paths.extend(str(root / file) for file in files if Path(file).suffix.lower() not in IGNORE_EXTENSIONS)
    return paths


def get_index(paths: set):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(_scan_dir, paths)

    return [path for paths in results for path in paths]
