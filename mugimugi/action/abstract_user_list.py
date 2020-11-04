from __future__ import annotations

from typing import ClassVar, Iterable, Iterator, TypeVar, Union

from enum import Enum

from dataclasses import dataclass

from ..enum import ElementNode
from ..configuration import REQUEST_EDIT_LIST_MAX_COUNT
from .abstract import AbstractAction


class Parameter(Enum):
    ID = "ID"


T = TypeVar("T", bound="AbstractUserListAction")


@dataclass
class AbstractUserListAction(AbstractAction):
    CONTENT_SEPARATOR: ClassVar[str] = ","
    BOOK_ID_PREFIX: ClassVar[str] = ElementNode.BOOK.value
    # Beyond this count, books are ignored.
    MAX_COUNT_OF_BOOK = REQUEST_EDIT_LIST_MAX_COUNT

    books: set[int]

    def __init__(self, books: Iterable[int]):
        self.books = set(books)

    def items(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().items()

        p = self.BOOK_ID_PREFIX
        yield Parameter.ID.value, self.CONTENT_SEPARATOR.join(
            p + str(b) for b in self.books
        )

    @classmethod
    def get_from_typed_id(cls: T, books: Iterable[str]) -> T:
        return cls.__init__(int(b[1:]) for b in books)
