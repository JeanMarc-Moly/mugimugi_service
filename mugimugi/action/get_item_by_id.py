from typing import Iterable, Union

from fast_enum import FastEnum

from ..enum import Action, ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"  # ItemType + int


class GetItemById(AbstractAction):
    IDS_SEPARATOR = ","

    def __init__(self, ids: Iterable[tuple[int, Union[str, ItemType]]]):
        self.ids = ids = {(id_, ItemType[type_]) for id_, type_ in ids}
        if not ids:
            raise Exception("Require at least one id")

    @staticmethod
    def get_action() -> Action:
        return Action.GET_ITEMS_BY_ID

    @property
    def params(self) -> dict[str, Union[int, str]]:
        params = super().params
        params[Parameter.ID.value] = self.IDS_SEPARATOR.join(
            type_.value + str(id_) for id_, type_ in self.ids
        )
        return params
