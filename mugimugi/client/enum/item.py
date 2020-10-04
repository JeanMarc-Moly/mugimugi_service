from fast_enum.fastenum import FastEnum


class ItemType(metaclass=FastEnum):
    AUTHOR = "AUTHOR"
    BOOK = "BOOK"
    CIRCLE = "CIRCLE"
    GENRE = "GENRE"
    CHARACTER = "CHARACTER"
    IMPRINT = "IMPRINT"
    CONTENT = "CONTENT"
    PUBLISHER = "PUBLISHER"
    CONVENTION = "CONVENTION"
    COLLECTIONS = "COLLECTIONS"
    PARODY = "PARODY"
    USER = "USER"
    TYPE = "TYPE"
