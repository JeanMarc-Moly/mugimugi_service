from enum import Enum
from typing import ClassVar, Iterator, Union

from ..enum import Action


class Parameter(Enum):
    ACTION = "S"  # Action


class AbstractAction:
    ACTION: ClassVar[Action]

    def __iter__(self) -> Iterator[Iterator[tuple[str, Union[str, int]]]]:
        yield self.items()

    def items(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield Parameter.ACTION.value, self.ACTION.value
