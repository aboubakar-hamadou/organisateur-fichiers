CATEGORIES: dict[str, list[str]] = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".odt"],
    "tableurs": [".xls", ".xlsx", ".csv", ".ods"],
    "archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "code": [".py", ".js", ".html", ".css", ".json"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "audio": [".mp3", ".wav", ".flac"],
}


def trouver_categorie(extension: str) -> str:
    """Retourne la catégorie d'une extension, ou 'autres' si inconnue."""
    extension = extension.lower()
    for categorie, extensions in CATEGORIES.items():
        if extension in extensions:
            return categorie
    return "autres"