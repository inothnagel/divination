from abc import ABC

from src.deck import Deck


class Spread(ABC):
    def consume(self, deck: Deck) -> None:
        """Consume cards from the deck and place them in the spread in order."""
        pass


class ThreeCardSpread(Spread):
    """The classic spread of three cards: The past, present, and future."""

    def __init__(self) -> None:
        super().__init__()
        # todo use a position class
        self.positions = {
            "past": None,
            "present": None,
            "future": None,
        }

    def consume(self, deck: Deck) -> None:
        for position in self.positions:
            try:
                self.positions[position] = next(deck)
            except StopIteration:
                raise ValueError("Deck is empty")

    def __str__(self) -> str:
        return f"Past: {self.positions['past']}, Present: {self.positions['present']}, Future: {self.positions['future']}"
