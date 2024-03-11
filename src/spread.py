from dataclasses import dataclass

from src.card import Card
from src.deck import Deck


@dataclass
class Position:
    name: str
    description: str
    card: Card | None

    @staticmethod
    def from_dict(data: dict) -> "Position":
        return Position(name=data["name"], description=data["description"], card=None)


@dataclass
class Spread:
    name: str
    description: str
    question: str | None
    positions: list[Position]

    @staticmethod
    def from_dict(data: dict) -> "Spread":
        positions = [Position.from_dict(pos) for pos in data["positions"]]
        return Spread(
            name=data["name"],
            description=data["description"],
            question=None,
            positions=positions,
        )

    def consume(self, deck: Deck) -> None:
        for position in self.positions:
            try:
                position.card = next(deck)
            except StopIteration:
                raise ValueError("Deck is empty")

    def __str__(self) -> str:
        position_str = ", ".join([f"{pos.name}: {pos.card}" for pos in self.positions])
        output = """
        Spread: {name}
        Description: {description}
        Question: {question}
        Positions: {position_str}
        """.format(
            name=self.name,
            description=self.description,
            question=self.question,
            position_str=position_str,
        )
        return output
