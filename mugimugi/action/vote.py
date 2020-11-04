from dataclasses import InitVar, dataclass
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Union

from ..configuration import REQUEST_VOTE_MAX_COUNT
from ..enum import Action, ElementPrefix, Score
from .abstract import AbstractAction
from .abstract_identifier import Parameter


class Parameter(Enum):
    ID = "ID"  # ElementNode + int
    SCORE = "score"  # Score


@dataclass
class Vote(AbstractAction):
    # TODO: instead of splitting ids, check on each result what is missing, would be a little faster on non-concurrent
    ACTION: ClassVar[Action] = Action.VOTE
    MAX_QUERY: ClassVar[int] = REQUEST_VOTE_MAX_COUNT
    IDS_SEPARATOR: ClassVar[str] = ","

    ids: InitVar[list[int]]
    score: Score

    def __post_init__(self, ids: Iterable[int]):
        self.ids = ids = list(set(ids))
        if not ids:
            raise Exception("Require at least one id")

    def __iter__(self) -> Iterator[Iterator[tuple[str, Union[str, int]]]]:
        cursor = 0
        chunk_size = self.MAX_QUERY
        ids = self.ids
        end = len(self.ids)
        while cursor < end:
            chunk_start = cursor
            cursor = cursor + chunk_size
            self.ids = ids[chunk_start:cursor]
            yield self

    def items(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().items()
        type_ = ElementPrefix.BOOK.value
        yield Parameter.ID.value, self.IDS_SEPARATOR.join(
            type_ + str(id_) for id_ in self.ids
        )
        yield Parameter.SCORE.value, self.score.value
