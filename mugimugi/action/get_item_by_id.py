from typing import Union

from fast_enum import FastEnum

from ..enum import Action, ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"  # ItemType + int


class GetItemById(AbstractAction):
    def __init__(
        self, id: int, type_: Union[str, ItemType],
    ):
        self.id = id
        self.type_ = ItemType(type_)

    @staticmethod
    def get_action() -> Action:
        return Action.GET_ITEM_BY_ID

    @property
    def params(self) -> dict[str, str]:
        params = super().params
        params[Parameter.ID.value] = self.type_.value + str(self.id)
        return params
