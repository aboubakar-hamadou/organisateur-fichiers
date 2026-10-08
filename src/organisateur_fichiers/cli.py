import argparse
from pathlib import Path

from organisateur_fichiers import journal
from organisateur_fichiers.executeur import annuler, executer
from organisateur_fichiers.scanner import planifier


def creer_parseur() -> argparse.ArgumentParser:
    parseur = argparse.ArgumentParser(
        description="Range les fichiers d'un dossier par catégorie"
    )
    parseur.add_argument("dossier", type=Path, help="Dossier à ranger")
    parseur.add_argument(
        "--dry-run", action="store_true", help="Simule sans déplacer"
    )
    parseur.add_argument(
        "--undo", action="store_true", help="Annule le dernier rangement"
    )
    return parseur


def main() -> None:
    args = creer_parseur().parse_args()
    dossier: Path = args.dossier

    try:
        if args.undo:
            annuler(journal.charger(dossier), dry_run=args.dry_run)
            if not args.dry_run:
                journal.supprimer(dossier)
        else:
            effectues = executer(planifier(dossier), dry_run=args.dry_run)
            if not args.dry_run:
                journal.sauvegarder(dossier, effectues)
    except (NotADirectoryError, FileNotFoundError) as erreur:
        print(f"Erreur : {erreur}")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()