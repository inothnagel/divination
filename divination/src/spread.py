from pydantic import BaseModel

from divination.src.deck import Deck
from divination.src.position import Position


class Spread(BaseModel):
    """A spread is a collection of positions that are used to interpret a reading."""

    name: str
    description: str
    positions: list[Position]

    def consume(self, deck: Deck) -> None:
        """Draw a card from the deck for each position in the spread."""
        for position in self.positions:
            try:
                position.card = next(deck)
            except StopIteration:
                raise ValueError("Deck is empty")

    def __str__(self) -> str:
        output_lines = [
            f"Spread: {self.name}",
            f"Description: {self.description}",
            "",
        ]
        for position in self.positions:
            output_lines.append(f"Position: {position.name}")
            output_lines.append(f"Description: {position.description}")
            if position.card:
                output_lines.append(f"Card: {position.card.name}")
            output_lines.append("")

        output = "\n".join(output_lines)
        return output
