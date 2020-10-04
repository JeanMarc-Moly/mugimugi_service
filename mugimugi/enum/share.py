from fast_enum import FastEnum


class Share(metaclass=FastEnum):
    NOT_SET = 0
    VERY_FEW = 1
    SOME = 2
    MANY = 3
    MOST = 4
    ALL = 5
