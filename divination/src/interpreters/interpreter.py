from abc import ABC, abstractmethod

from divination.src.reading import Reading


class Interpreter(ABC):
    """An abstract class for interpreting readings."""

    @abstractmethod
    def interpret(self, reading: Reading) -> str:
        pass
