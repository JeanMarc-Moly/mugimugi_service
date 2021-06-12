from enum import Enum


class ElementNode(Enum):
    LIST = "LIST"
    ERROR = "ERROR"
    ITEM = "ITEM"
    LINK = "LINKS"

    AUTHOR = "AUTHOR"
    BOOK = "BOOK"
    CIRCLE = "CIRCLE"
    GENRE = "GENRE"
    CHARACTER = "CHARACTER"
    IMPRINT = "IMPRINT"
    CONTENT = "CONTENT"
    PUBLISHER = "PUBLISHER"
    CONVENTION = "CONVENTION"
    COLLECTION = "COLLECTIONS"
    PARODY = "PARODY"
    USER = "USER"
    TYPE = "TYPE"
