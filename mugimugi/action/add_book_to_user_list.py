from dataclasses import dataclass
from typing import ClassVar

from ..enum import Action
from .abstract_user_list import AbstractUserListAction


@dataclass
class AddBookToUserList(AbstractUserListAction):
    ACTION: ClassVar[Action] = Action.ADD_BOOK_TO_USER_LIST
