from src.deck import Deck
import yaml

from src.spread import Spread


def main() -> None:

    # Assuming you have a YAML file named 'example.yml'
    with open("../data/spreads/celtic-cross-spread.yml", "r") as file:
        data = yaml.safe_load(file)

    spread = Spread.from_dict(data)

    deck = Deck("../data/thoth.json")
    deck.shuffle()

    spread.consume(deck)
    print(spread)


if __name__ == "__main__":
    main()
