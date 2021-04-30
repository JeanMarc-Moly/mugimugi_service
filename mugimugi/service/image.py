from typing import AsyncIterator, Iterable

from multimethod import multimethod


class Image:
    ...


# class Image(metaclass=multimethod):
# def get(id_: int) -> Entity:
#     raise Exception("Not Implemented")

# def get(id_: str) -> Entity:
#     raise Exception("Not Implemented")

# def get(ids: set[str]) -> Entity:
#     raise Exception("Not Implemented")

# def get(ids: Iterable[int]) -> AsyncIterator[Entity]:
#     raise Exception("Not Implemented")

# def search(**kwargs) -> AsyncIterator[Entity]:
#     raise Exception("Not Implemented")

# def add(**kwargs) -> Entity:
#     raise Exception("Not Implemented")

# def edit(**kwargs) -> Entity:
#     raise Exception("Not Implemented")

# def delete(**kwargs) -> Entity:
#     raise Exception("Not Implemented")
