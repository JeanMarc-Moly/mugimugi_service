from enum import Enum
from typing import Iterator


class ElementPrefix(Enum):
    AUTHOR = "A"
    BOOK = "B"
    CHARACTER = "H"
    CIRCLE = "C"
    COLLECTION = "O"
    CONTENT = "K"
    CONVENTION = "N"
    GENRE = "G"
    IMPRINT = "I"
    PARODY = "P"
    PUBLISHER = "L"
    TYPE = "T"

    @classmethod
    def values(cls) -> Iterator[str]:
        for t in cls:
            yield t.value
