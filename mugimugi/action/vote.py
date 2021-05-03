from dataclasses import InitVar, dataclass
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Union

from ..configuration import REQUEST_VOTE_MAX_COUNT
from ..enum import Action, ElementPrefix, Score
from .abstract_by_chunk import AbstractActionByChunk
from ..entity.main import Book


@dataclass
class Vote(AbstractActionByChunk):
    class Parameter(Enum):
        SCORE = "score"  # Score

    _ACTION: ClassVar[Action] = Action.VOTE
    _CHUNK_SIZE: ClassVar[int] = REQUEST_VOTE_MAX_COUNT

    book_ids: InitVar[Iterable[int]]
    score: Score

    @classmethod
    @property
    def ACTION(cls) -> Action:
        return cls._ACTION

    @classmethod
    @property
    def CHUNK_SIZE(self) -> int:
        return self._CHUNK_SIZE

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Book.PREFIX

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()
        yield self.Parameter.SCORE.value, self.score.value
