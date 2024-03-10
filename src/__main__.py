from src.deck import Deck
from src.spread import ThreeCardSpread


def main() -> None:
    deck = Deck("../data/thoth.json")
    deck.shuffle()
    spread = ThreeCardSpread()
    spread.consume(deck)
    print(spread)


if __name__ == "__main__":
    main()
