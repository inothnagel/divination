import json

import yaml

from src.deck import Deck
from src.spread import Spread


def load_deck() -> Deck:
    deck_data_path = "../data/thoth.json"
    with open(deck_data_path, "r") as file:
        deck_data = json.load(file)
    return Deck.parse_obj(deck_data)


def load_spread() -> Spread:
    spread_data_path = "../data/spreads/celtic-cross-spread.yml"
    with open(spread_data_path, "r") as file:
        data = yaml.safe_load(file)
    return Spread.parse_obj(data)


def main() -> None:
    deck = load_deck()
    deck.shuffle()

    spread = load_spread()
    spread.consume(deck)

    print(spread)


if __name__ == "__main__":
    main()
