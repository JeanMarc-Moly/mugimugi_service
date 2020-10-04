from fast_enum import FastEnum


class Gender(metaclass=FastEnum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2
    ANIMAL = 3
    ROBOT = 4
