from fast_enum import FastEnum


class ItemType(metaclass=FastEnum):
    AUTHOR = "A"
    BOOK = "B"
    CIRCLE = "C"
    GENRE = "G"
    CHARACTER = "H"
    IMPRINT = "I"
    CONTENTS = "K"
    PUBLISHER = "L"
    CONVENTION = "N"
    COLLECTIONS = "O"
    PARODY = "P"
    TYPE = "T"
