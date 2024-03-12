import json
import os

import toml
import yaml
from dotenv import load_dotenv

from divination.src.deck import Deck
from divination.src.interpreters.open_ai_interpreter import OpenAIInterpreter
from divination.src.reading import Reading
from divination.src.spread import Spread

load_dotenv()


def load_deck() -> Deck:
    deck_data_path = "data/decks/thoth.json"
    with open(deck_data_path, "r") as file:
        deck_data = json.load(file)
    deck = Deck.parse_obj(deck_data)
    deck.shuffle()
    return deck


def load_spread() -> Spread:
    spread_data_path = "data/spreads/celtic-cross-spread.yml"
    with open(spread_data_path, "r") as file:
        data = yaml.safe_load(file)
    return Spread.parse_obj(data)


def main() -> None:
    config_file_path = "config.toml"
    config = toml.load(config_file_path)

    question = input("What is your question? ")

    deck = load_deck()
    spread = load_spread()
    reading = Reading(deck, spread, question)
    interpreter = OpenAIInterpreter(api_key=os.environ["OPENAI_API_KEY"], config=config)
    response = interpreter.interpret(reading)

    print(reading)
    print(response)


if __name__ == "__main__":
    main()
