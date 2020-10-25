from typing import ClassVar, Optional

from .client import Client
from .configuration import API_KEY
from .service import *


class MugiMugi:
    HOST_NAME: ClassVar[str] = "https://www.doujinshi.org/"
    API_PATH: ClassVar[str] = "api/"

    # lxml do not like unicode declaration.
    DECLARATION: ClassVar[str] = """<?xml version="1.0" encoding="UTF-8"?>\n"""
    DECLARATION_LENGTH: ClassVar[int] = len(DECLARATION)

    _author: Optional[Author] = None
    # _book: Optional[Book] = None
    _character: Optional[Character] = None
    _circle: Optional[Circle] = None
    _collection: Optional[Collection] = None
    _content: Optional[Content] = None
    _convention: Optional[Convention] = None
    _genre: Optional[Genre] = None
    # _image: Optional[Image] = None
    _imprint: Optional[Imprint] = None
    # _list: Optional[List] = None
    _parody: Optional[Parody] = None
    _publisher: Optional[Publisher] = None
    # _type: Optional[Type] = None

    def __init__(self, key: str = API_KEY) -> None:
        self.api_client = Client(key)

    @property
    def author(self) -> Author:
        if (author := self._author) is None:
            self._author = author = Author(self.api_client)
        return author

    # @property
    # def book(self) -> Book:
    #     if(book := self._book) is None:
    #         self._book = book = Book(self.api_client)
    #     return book

    @property
    def character(self) -> Character:
        if(character := self._character) is None:
            self._character = character = Character(self.api_client)
        return character

    @property
    def circle(self) -> Circle:
        if(circle := self._circle) is None:
            self._circle = circle = Circle(self.api_client)
        return circle

    @property
    def collection(self) -> Collection:
        if(collection := self._collection) is None:
            self._collection = collection = Collection(self.api_client)
        return collection

    @property
    def content(self) -> Content:
        if(content := self._content) is None:
            self._content = content = Content(self.api_client)
        return content

    @property
    def convention(self) -> Convention:
        if(convention := self._convention) is None:
            self._convention = convention = Convention(self.api_client)
        return convention

    @property
    def genre(self) -> Genre:
        if(genre := self._genre) is None:
            self._genre = genre = Genre(self.api_client)
        return genre

    # @property
    # def image(self) -> Image:
    #     if(image := self._image) is None:
    #         self._image = image = Image(self.api_client)
    #     return image

    @property
    def imprint(self) -> Imprint:
        if(imprint := self._imprint) is None:
            self._imprint = imprint = Imprint(self.api_client)
        return imprint

    # @property
    # def list(self) -> List:
    #     if(list := self._list) is None:
    #         self._list = list = List(self.api_client)
    #     return list

    @property
    def parody(self) -> Parody:
        if(parody := self._parody) is None:
            self._parody = parody = Parody(self.api_client)
        return parody

    @property
    def publisher(self) -> Publisher:
        if(publisher := self._publisher) is None:
            self._publisher = publisher = Publisher(self.api_client)
        return publisher

    # @property
    # def type(self) -> Type:
    #     if(type := self._type) is None:
    #         self._type = type = Type(self.api_client)
    #     return type