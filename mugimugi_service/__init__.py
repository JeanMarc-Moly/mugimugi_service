from functools import cached_property

from mugimugi_client_api import MugiMugiClient

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


class MugiMugi(MugiMugiClient):
    @cached_property
    def author(self) -> Author:
        return Author(self)

    @cached_property
    def book(self) -> Book:
        return Book(self)

    @cached_property
    def character(self) -> Character:
        return Character(self)

    @cached_property
    def circle(self) -> Circle:
        return Circle(self)

    @cached_property
    def collection(self) -> Collection:
        return Collection(self)

    @cached_property
    def content(self) -> Content:
        return Content(self)

    @cached_property
    def convention(self) -> Convention:
        return Convention(self)

    @cached_property
    def genre(self) -> Genre:
        return Genre(self)

    @cached_property
    def imprint(self) -> Imprint:
        return Imprint(self)

    @cached_property
    def parody(self) -> Parody:
        return Parody(self)

    @cached_property
    def publisher(self) -> Publisher:
        return Publisher(self)

    @cached_property
    def user(self) -> User:
        return User(self)
