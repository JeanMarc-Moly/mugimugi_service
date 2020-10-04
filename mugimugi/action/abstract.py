from abc import abstractstaticmethod
from fast_enum import FastEnum

from ..enum import Action


class Parameter(metaclass=FastEnum):
    ACTION = "S"  # Action


class AbstractAction:
    @abstractstaticmethod
    def get_action() -> Action:
        ...

    @property
    def params(self):
        return {Parameter.ACTION.value: self.get_action().value}
