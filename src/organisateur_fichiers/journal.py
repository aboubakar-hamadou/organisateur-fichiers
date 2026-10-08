import json
from datetime import UTC, datetime
from pathlib import Path

from organisateur_fichiers.modeles import Deplacement

NOM_JOURNAL = ".organisateur_journal.json"


def sauvegarder(dossier: Path, deplacements: list[Deplacement]) -> None:
    """Enregistre les déplacements effectués pour pouvoir les annuler."""
    if not deplacements:
        return
    donnees = {
        "date": datetime.now(UTC).isoformat(timespec="seconds"),
        "deplacements": [
            {"source": str(d.source), "destination": str(d.destination)}
            for d in deplacements
        ],
    }
    chemin = dossier / NOM_JOURNAL
    chemin.write_text(json.dumps(donnees, indent=2), encoding="utf-8")


def charger(dossier: Path) -> list[Deplacement]:
    """Relit le dernier journal, ou lève FileNotFoundError s'il n'existe pas."""
    chemin = dossier / NOM_JOURNAL
    try:
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise FileNotFoundError("Aucun journal trouvé : rien à annuler") from None
    return [
        Deplacement(Path(d["source"]), Path(d["destination"]))
        for d in donnees["deplacements"]
    ]


def supprimer(dossier: Path) -> None:
    (dossier / NOM_JOURNAL).unlink(missing_ok=True)
