from typing import Optional

from .client import Client
from .service import *


class MugiMugi:
    _author: Optional[Author] = None
    _book: Optional[Book] = None
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
    _user: Optional[User] = None

    def __init__(self, key: str) -> None:
        self.api_client = Client(key)

    @property
    def author(self) -> Author:
        if (author_ := self._author) is None:
            self._author = author_ = Author(self.api_client)
        return author_

    @property
    def book(self) -> Book:
        if (book := self._book) is None:
            self._book = book = Book(self.api_client)
        return book

    @property
    def character(self) -> Character:
        if (character_ := self._character) is None:
            self._character = character_ = Character(self.api_client)
        return character_

    @property
    def circle(self) -> Circle:
        if (circle_ := self._circle) is None:
            self._circle = circle_ = Circle(self.api_client)
        return circle_

    @property
    def collection(self) -> Collection:
        if (collection_ := self._collection) is None:
            self._collection = collection_ = Collection(self.api_client)
        return collection_

    @property
    def content(self) -> Content:
        if (content_ := self._content) is None:
            self._content = content_ = Content(self.api_client)
        return content_

    @property
    def convention(self) -> Convention:
        if (convention_ := self._convention) is None:
            self._convention = convention_ = Convention(self.api_client)
        return convention_

    @property
    def genre(self) -> Genre:
        if (genre_ := self._genre) is None:
            self._genre = genre_ = Genre(self.api_client)
        return genre_

    # @property
    # def image(self) -> Image:
    #     if(image := self._image) is None:
    #         self._image = image = Image(self.api_client)
    #     return image

    @property
    def imprint(self) -> Imprint:
        if (imprint_ := self._imprint) is None:
            self._imprint = imprint_ = Imprint(self.api_client)
        return imprint_

    # @property
    # def list(self) -> List:
    #     if(list := self._list) is None:
    #         self._list = list = List(self.api_client)
    #     return list

    @property
    def parody(self) -> Parody:
        if (parody_ := self._parody) is None:
            self._parody = parody_ = Parody(self.api_client)
        return parody_

    @property
    def publisher(self) -> Publisher:
        if (publisher_ := self._publisher) is None:
            self._publisher = publisher_ = Publisher(self.api_client)
        return publisher_

    # @property
    # def type(self) -> Type:
    #     if(type_ := self._type) is None:
    #         self._type = type_ = Type(self.api_client)
    #     return type_

    @property
    def user(self) -> User:
        if (user_ := self._user) is None:
            self._user = user_ = User(self.api_client)
        return user_
