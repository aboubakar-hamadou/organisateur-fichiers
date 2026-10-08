from pathlib import Path

from organisateur_fichiers.categories import trouver_categorie
from organisateur_fichiers.modeles import Deplacement


def planifier(dossier: Path) -> list[Deplacement]:
    """Prépare la liste des déplacements, sans toucher aux fichiers."""
    if not dossier.is_dir():
        raise NotADirectoryError(f"Dossier introuvable : {dossier}")

    deplacements: list[Deplacement] = []
    for fichier in dossier.iterdir():
        if not fichier.is_file() or fichier.name.startswith("."):
            continue
        categorie = trouver_categorie(fichier.suffix)
        destination = dossier / categorie / fichier.name
        deplacements.append(Deplacement(fichier, destination))
    return deplacements