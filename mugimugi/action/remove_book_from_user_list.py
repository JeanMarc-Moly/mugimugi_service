from dataclasses import dataclass
from typing import ClassVar
from .abstract_user_list import AbstractUserListAction
from ..enum import Action


@dataclass
class RemoveBookFromUserList(AbstractUserListAction):
    ACTION: ClassVar[Action] = Action.REMOVE_BOOK_FROM_USER_LIST
