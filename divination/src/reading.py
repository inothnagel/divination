from divination.src.deck import Deck
from divination.src.spread import Spread


class Reading:
    """A card reading that includes a question, a deck, and a spread."""

    def __init__(self, deck: Deck, spread: Spread, question: str):
        self.deck = deck
        self.spread = spread
        self.question = question
        self.spread.consume(deck)

    def __str__(self):
        output_lines = [
            f"Question: {self.question}",
            "",
            str(self.spread),
        ]
        output = "\n".join(output_lines)
        return output

    @property
    def prompt(self):
        """Return a text description suitable for use as a prompt for an AI interpreter."""
        return self.__str__()
