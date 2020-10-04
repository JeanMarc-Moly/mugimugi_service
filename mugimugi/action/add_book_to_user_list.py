from .abstract_user_list import AbstractUserListAction
from ..enum import Action


class AddBookToUserList(AbstractUserListAction):
    @staticmethod
    def get_action() -> Action:
        return Action.ADD_BOOK_TO_USER_LIST
