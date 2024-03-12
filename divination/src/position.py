from typing import Optional

from pydantic import BaseModel

from divination.src.card import Card


class Position(BaseModel):
    """The position of a specific card in a tarot spread."""

    name: str
    description: str
    card: Optional[Card] = None
