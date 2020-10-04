from ...action import Vote as Action
from .abstract import SynchronousClient


class Vote(SynchronousClient, Action):
    ...
