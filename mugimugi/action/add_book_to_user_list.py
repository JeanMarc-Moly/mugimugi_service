from dataclasses import dataclass
from typing import ClassVar
from .abstract_user_list import AbstractUserListAction
from ..enum import Action


@dataclass
class AddBookToUserList(AbstractUserListAction):
    ACTION: ClassVar[Action] = Action.ADD_BOOK_TO_USER_LIST
