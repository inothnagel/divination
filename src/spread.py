from typing import Optional

from pydantic import BaseModel

from src.deck import Deck
from src.position import Position


class Spread(BaseModel):
    name: str
    description: str
    positions: list[Position]
    question: Optional[str] = None

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
