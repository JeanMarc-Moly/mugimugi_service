from mugimugi.bo.links import Item
from fast_enum import FastEnum


class ItemType(metaclass=FastEnum):
    AUTHOR = "A"
    BOOK = "B"
    CIRCLE = "C"
    GENRE = "G"
    CHARACTER = "H"
    IMPRINT = "I"
    CONTENT = "K"
    PUBLISHER = "L"
    CONVENTION = "N"
    COLLECTION = "O"
    PARODY = "P"
    TYPE = "T"
