import shutil

from organisateur_fichiers.modeles import Deplacement


def executer(
    deplacements: list[Deplacement], dry_run: bool = False
) -> list[Deplacement]:
    """Exécute les déplacements et retourne ceux réellement effectués."""
    effectues: list[Deplacement] = []

    for deplacement in deplacements:
        if dry_run:
            print(
                f"[SIMULATION] {deplacement.source.name}"
                f" -> {deplacement.destination.parent.name}/"
            )
            continue

        if deplacement.destination.exists():
            print(f"Ignoré (existe déjà) : {deplacement.destination}")
            continue

        try:
            deplacement.destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(deplacement.source), str(deplacement.destination))
        except PermissionError:
            print(f"Permission refusée : {deplacement.source}")
            continue

        effectues.append(deplacement)
        print(
            f"{deplacement.source.name}"
            f" -> {deplacement.destination.parent.name}/"
        )

    return effectues

def annuler(deplacements: list[Deplacement], dry_run: bool = False) -> None:
    """Remet les fichiers à leur place d'origine, dans l'ordre inverse."""
    for deplacement in reversed(deplacements):
        if not deplacement.destination.exists():
            print(f"Introuvable, ignoré : {deplacement.destination}")
            continue
        if deplacement.source.exists():
            print(f"Ignoré (la source existe déjà) : {deplacement.source}")
            continue

        if dry_run:
            print(f"[SIMULATION] {deplacement.destination.name} -> retour")
            continue

        shutil.move(str(deplacement.destination), str(deplacement.source))
        print(f"{deplacement.destination.name} -> retour")

        try:
            deplacement.destination.parent.rmdir()  # supprime le dossier s'il est vide
        except OSError:
            pass  # dossier non vide : on le laisse