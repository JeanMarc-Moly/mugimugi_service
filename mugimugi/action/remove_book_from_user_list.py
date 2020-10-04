from .abstract_user_list import AbstractUserListAction
from ..enum import Action


class RemoveBookFromUserList(AbstractUserListAction):
    @staticmethod
    def get_action() -> Action:
        return Action.REMOVE_BOOK_FROM_USER_LIST
