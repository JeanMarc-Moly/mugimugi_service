from __future__ import annotations

from asyncio import wait
from functools import cached_property
from types import TracebackType
from typing import AsyncContextManager, Optional

from .api import API
from .author import Author
from .book import Book
from .character import Character
from .circle import Circle
from .collection import Collection
from .content import Content
from .convention import Convention
from .genre import Genre
from .imprint import Imprint
from .parody import Parody
from .publisher import Publisher
from .user import User


class MugiMugi(AsyncContextManager):
    api: API

    def __init__(self, key: str):
        self.api = API(key)

    async def __aenter__(self) -> MugiMugi:
        await wait({self.api.data.__aenter__(), self.api.image.__aenter__()})
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool:
        await wait({self.api.data.__aexit__(), self.api.image.__aexit__()})
        return True

    @cached_property
    def author(self) -> Author:
        return Author(self.api)

    @cached_property
    def book(self) -> Book:
        return Book(self.api)

    @cached_property
    def character(self) -> Character:
        return Character(self.api)

    @cached_property
    def circle(self) -> Circle:
        return Circle(self.api)

    @cached_property
    def collection(self) -> Collection:
        return Collection(self.api)

    @cached_property
    def content(self) -> Content:
        return Content(self.api)

    @cached_property
    def convention(self) -> Convention:
        return Convention(self.api)

    @cached_property
    def genre(self) -> Genre:
        return Genre(self.api)

    @cached_property
    def imprint(self) -> Imprint:
        return Imprint(self.api)

    @cached_property
    def parody(self) -> Parody:
        return Parody(self.api)

    @cached_property
    def publisher(self) -> Publisher:
        return Publisher(self.api)

    @cached_property
    def user(self) -> User:
        return User(self.api)
