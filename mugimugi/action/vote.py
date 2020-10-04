from fast_enum import FastEnum

from ..enum import Action, Score
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    SCORE = "score"


class Vote(AbstractAction):
    def __init__(self, score: str):
        super().__init__(Action.VOTE)
        self.score = Score[score]

    @property
    def params(self):
        params = super().params
        params[Parameter.SCORE.value] = self.score.value
        return params
