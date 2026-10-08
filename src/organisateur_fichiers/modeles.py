from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Deplacement:
    source: Path
    destination: Path

    def __post_init__(self) -> None:
        if self.source == self.destination:
            raise ValueError("La source et la destination sont identiques")
