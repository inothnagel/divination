from pydantic import BaseModel


class Card(BaseModel):
    id: str
    name: str

    def __str__(self) -> str:
        return f"{self.name}"
