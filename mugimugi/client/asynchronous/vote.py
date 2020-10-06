from ...action import Vote as Action
from .abstract import AsynchronousClient


class Vote(AsynchronousClient, Action):
    ...
