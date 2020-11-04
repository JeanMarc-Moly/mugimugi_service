from dataclasses import InitVar, dataclass
from enum import Enum
from typing import ClassVar, Iterable, Iterator, Tuple, Union

from ..configuration import REQUEST_GET_ID_MAX_COUNT
from ..enum import Action, ElementPrefix
from .abstract import AbstractAction


class Parameter(Enum):
    ID = "ID"  # ElementNode + int


@dataclass
class GetItemById(AbstractAction):
    # TODO: instead of splitting ids, check on each result what is missing, would be a little faster on non-concurrent
    ACTION: ClassVar[Action] = Action.GET_ITEMS_BY_ID
    MAX_QUERY: ClassVar[int] = REQUEST_GET_ID_MAX_COUNT
    IDS_SEPARATOR: ClassVar[str] = ","

    ids: InitVar[list[Tuple[ElementPrefix, int]]]

    def __post_init__(self, ids: Iterable[Tuple[ElementPrefix, int]]):
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
        yield Parameter.ID.value, self.IDS_SEPARATOR.join(
            type_.value + str(id_) for type_, id_ in self.ids
        )
