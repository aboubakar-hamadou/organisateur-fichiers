from pathlib import Path

from organisateur_fichiers.categories import trouver_categorie
from organisateur_fichiers.modeles import Deplacement


def planifier(
    dossier: Path, exclure: set[str] | None = None
) -> list[Deplacement]:
    """Prépare la liste des déplacements, sans toucher aux fichiers."""
    if not dossier.is_dir():
        raise NotADirectoryError(f"Dossier introuvable : {dossier}")

    exclusions = exclure or set()
    deplacements: list[Deplacement] = []
    for fichier in dossier.iterdir():
        if not fichier.is_file() or fichier.name.startswith("."):
            continue
        if fichier.suffix.lower() in exclusions:
            continue
        categorie = trouver_categorie(fichier.suffix)
        destination = dossier / categorie / fichier.name
        deplacements.append(Deplacement(fichier, destination))
    return deplacements