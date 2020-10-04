from typing import Type
from fast_enum.fastenum import FastEnum
from ...error import *


class Error(metaclass=FastEnum):
    error: Type
    __slots__ = ("error",)

    UNKNOWN = "0", Unknown
    NO_QUERY_LEFT = "2", NoQueryLeft
    INVALID_SCORE = "11", InvalidScore
    API_KEY_NOT_FOUND = "1", ApiKeyNotFound
    ID_NOT_FOUND = "9", IdNotFound
    OBJECT_NOT_FOUND = "10", ObjectNotFound
    USER_NOT_FOUND = "8", UserNotFound
    IMAGE_NOT_FOUND = "5", ImageNotFound
    IMAGE_NOT_RECEIVED = "7", ImageNotReceived
    IMAGE_NOT_UPLOADED = "3", ImageNotUploaded
    IMAGE_SEARCH_SERVER_DOWN = "6", ImageServerDown
    IMAGE_TOO_BIG = "4", ImageTooBig

    def __init__(self, value: int, error: Type, name: str):
        self.value = value
        self.name = name
        self.error = error
