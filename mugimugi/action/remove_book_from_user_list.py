from dataclasses import dataclass
from typing import ClassVar

from ..enum import Action
from .abstract_user_list import AbstractUserListAction


@dataclass
class RemoveBookFromUserList(AbstractUserListAction):
    ACTION: ClassVar[Action] = Action.REMOVE_BOOK_FROM_USER_LIST
