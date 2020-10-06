from ...action import AddBookToUserList as Action
from .abstract import SynchronousClient


class AddBookToUserList(SynchronousClient, Action):
    ...
