from dataclasses import dataclass


@dataclass
class Card:
    ident: str
    name: str

    def __str__(self) -> str:
        return f"{self.name}"
