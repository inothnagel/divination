import random
from typing import Iterator

from pydantic import BaseModel

from divination.src.card import Card


class Deck(BaseModel):
    cards: list[Card]

    def __iter__(self) -> Iterator[Card]:
        """Return the deck as an iterator. This allows the deck to be used as a generator."""
        return self

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw and remove a card from the deck. Raises IndexError if the deck is empty."""
        return self.cards.pop()

    def __next__(self) -> Card:
        """Generator method to draw a card from the deck. Raises StopIteration if the deck is empty."""
        if not self.cards:
            raise StopIteration
        return self.draw_card()
