from ...action import GetItemById as Action
from .abstract import SynchronousClient


class GetItemById(SynchronousClient, Action):
    ...
