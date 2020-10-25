from typing import Iterable, Tuple

from fast_enum import FastEnum

from ..enum import Action, ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"  # ItemType + int


class GetItemById(AbstractAction):
    IDS_SEPARATOR = ","
    MAX_QUERY = 100

    def __init__(self, ids: Iterable[Tuple[ItemType, int]]):
        self.ids = ids = set(ids)
        if not ids:
            raise Exception("Require at least one id")
        if (max := self.MAX_QUERY) < len(ids):
            raise Exception(f"Can not query more than {max}")

    @staticmethod
    def get_action() -> Action:
        return Action.GET_ITEMS_BY_ID

    @property
    def params(self) -> dict[str, str]:
        params = super().params
        params[Parameter.ID.value] = self.IDS_SEPARATOR.join(
            type_.value + str(id_) for type_, id_ in self.ids
        )
        return params
