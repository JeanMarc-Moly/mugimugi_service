from dataclasses import InitVar, dataclass, field
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Union

from ..configuration import REQUEST_VOTE_MAX_COUNT
from ..enum import Action, ElementPrefix, Score
from .abstract_by_chunk import AbstractActionByChunk


@dataclass
class Vote(AbstractActionByChunk):
    class Parameter(Enum):
        SCORE = "score"  # Score

    ACTION: ClassVar[Action] = Action.VOTE
    MAX_QUERY: ClassVar[int] = REQUEST_VOTE_MAX_COUNT

    book_ids: InitVar[Iterable[int]]
    score: Score

    def __post_init__(self, book_ids: Iterable[int]):
        self.ids = set((ElementPrefix.BOOK, id_) for id_ in book_ids)
        super().__post_init__()

    @property
    def action(self) -> Action:
        return self.ACTION

    @property
    def chunk_size(self) -> int:
        return self.MAX_QUERY

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()
        yield self.Parameter.SCORE.value, self.score.value
