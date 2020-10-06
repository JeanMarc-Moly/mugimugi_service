from fast_enum import FastEnum


class Action(metaclass=FastEnum):
    ADD_BOOK_TO_USER_LIST = "adduserlist"
    REMOVE_BOOK_FROM_USER_LIST = "deluserlist"
    GET_ITEM_BY_ID = "getID"
    SEARCH_IMAGE = "imageSearch"
    SEARCH_ITEM = "itemSearch"
    SEARCH_OBJECT = "objectSearch"
    VOTE = "vote"
