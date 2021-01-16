from typing import AsyncIterator, Iterable, Set
from multimethod import multimethod


from ..entity.image import Image as Entity


class Author(metaclass=multimethod):
    def get(id_: int) -> Entity:
        raise Exception("Not Implemented")

    def get(id_: str) -> Entity:
        raise Exception("Not Implemented")

    def get(ids: Set[str]) -> Entity:
        raise Exception("Not Implemented")

    def get(ids: Iterable[int]) -> AsyncIterator[Entity]:
        raise Exception("Not Implemented")

    def search(**kwargs) -> AsyncIterator[Entity]:
        raise Exception("Not Implemented")

    def add(**kwargs) -> Entity:
        raise Exception("Not Implemented")

    def edit(**kwargs) -> Entity:
        raise Exception("Not Implemented")

    def delete(**kwargs) -> Entity:
        raise Exception("Not Implemented")
