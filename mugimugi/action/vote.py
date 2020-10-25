from typing import Tuple, Union, Iterable
from fast_enum import FastEnum

from ..enum import Action, Score, ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"  # ItemType + int
    SCORE = "score"  # Score


class Vote(AbstractAction):
    IDS_SEPARATOR = ","
    MAX_QUERY = 25

    def __init__(self, ids: Iterable[Tuple[ItemType, int]], score: Score):
        self.ids = ids = set(ids)
        if not ids:
            raise Exception("Require at least one id")
        if (max := self.MAX_QUERY) < len(ids):
            raise Exception(f"Can not query more than {max}")
        self.score = score

    @staticmethod
    def get_action() -> Action:
        return Action.VOTE

    @property
    def params(self) -> dict[str, Union[int, str]]:
        params = super().params
        params[Parameter.ID.value] = self.IDS_SEPARATOR.join(
            type_.value + str(id_) for id_, type_ in self.ids
        )
        params[Parameter.SCORE.value] = self.score.value
        return params
