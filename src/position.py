from typing import Optional

from pydantic import BaseModel

from src.card import Card


class Position(BaseModel):
    name: str
    description: str
    card: Optional[Card] = None
