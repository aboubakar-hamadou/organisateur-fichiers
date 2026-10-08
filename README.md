# Organisateur de fichiers

Outil en ligne de commande qui range les fichiers d'un dossier par catégorie
(images, documents, archives, code...), avec simulation et annulation.

## Installation

Nécessite [uv](https://docs.astral.sh/uv/) et Python 3.14.

```bash
git clone git@github.com:aboubakar-hamadou/organisateur-fichiers.git
cd organisateur-fichiers
uv sync
```

## Utilisation

```bash
uv run organiser ~/Téléchargements --dry-run   # simule, ne déplace rien
uv run organiser ~/Téléchargements             # range les fichiers
uv run organiser ~/Téléchargements --undo      # annule le dernier rangement
```

## Fonctionnement

1. `scanner.py` planifie les déplacements sans toucher aux fichiers.
2. `executeur.py` les exécute (ou les simule avec `--dry-run`).
3. `journal.py` enregistre les déplacements effectués en JSON, ce qui permet `--undo`.

Un fichier existant n'est jamais écrasé.

## Structure

```
src/organisateur_fichiers/
├── categories.py   # extensions -> catégories
├── modeles.py      # dataclass Deplacement
├── scanner.py      # planification
├── executeur.py    # exécution et annulation
├── journal.py      # sauvegarde JSON
└── cli.py          # options argparse
```