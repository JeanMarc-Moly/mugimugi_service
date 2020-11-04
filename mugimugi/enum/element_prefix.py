from enum import Enum
from typing import Iterator


class ElementPrefix(Enum):
    AUTHOR = "A"
    BOOK = "B"
    CIRCLE = "C"
    GENRE = "G"
    CHARACTER = "H"
    IMPRINT = "I"
    CONTENT = "K"
    PUBLISHER = "L"
    CONVENTION = "N"
    COLLECTION = "O"
    PARODY = "P"
    TYPE = "T"

    @classmethod
    def values(cls) -> Iterator[str]:
        for t in cls:
            yield t.value
