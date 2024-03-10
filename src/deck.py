import json
import random
from typing import Iterator

from src.card import Card


class Deck:
    def __init__(self, deck_data_path: str) -> None:
        self.cards = []
        self.build(deck_data_path)

    def __iter__(self) -> Iterator[Card]:
        """Return the deck as an iterator. This allows the deck to be used as a generator."""
        return self

    def build(self, deck_data_path) -> None:
        """Build the deck from a JSON file."""
        try:
            with open(deck_data_path) as f:
                data = json.load(f)
                for card_data in data:
                    self.cards.append(Card(card_data["id"], card_data["name"]))
        except FileNotFoundError:
            raise FileNotFoundError(f"Deck data file not found at: {deck_data_path}")

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
