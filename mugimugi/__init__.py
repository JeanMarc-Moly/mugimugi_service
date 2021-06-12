from __future__ import annotations

from typing import Any, ClassVar, Optional

from httpx import AsyncClient, Request
from httpx._client import (
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
)

from .configuration import API_PATH
from .service import *


class MugiMugi(AsyncClient):
    API: ClassVar[str] = API_PATH

    _author: Optional[Author] = None
    _book: Optional[Book] = None
    _character: Optional[Character] = None
    _circle: Optional[Circle] = None
    _collection: Optional[Collection] = None
    _content: Optional[Content] = None
    _convention: Optional[Convention] = None
    _genre: Optional[Genre] = None
    _image: Optional[Image] = None
    _imprint: Optional[Imprint] = None
    _favorite: Optional[Favorite] = None
    _parody: Optional[Parody] = None
    _publisher: Optional[Publisher] = None
    # _type: Optional[Type] = None
    _user: Optional[User] = None

    def __init__(self, key: str) -> None:
        super().__init__(base_url=self.API.format(key=key))

    def build_request(
        self,
        method: str,
        *,
        content: RequestContent = None,
        data: RequestData = None,
        files: RequestFiles = None,
        json: Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
    ) -> Request:
        return super().build_request(
            method,
            url=self._base_url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
        )

    @property
    def author(self) -> Author:
        if (author_ := self._author) is None:
            self._author = author_ = Author(self)
        return author_

    @property
    def book(self) -> Book:
        if (book_ := self._book) is None:
            self._book = book_ = Book(self)
        return book_

    @property
    def character(self) -> Character:
        if (character_ := self._character) is None:
            self._character = character_ = Character(self)
        return character_

    @property
    def circle(self) -> Circle:
        if (circle_ := self._circle) is None:
            self._circle = circle_ = Circle(self)
        return circle_

    @property
    def collection(self) -> Collection:
        if (collection_ := self._collection) is None:
            self._collection = collection_ = Collection(self)
        return collection_

    @property
    def content(self) -> Content:
        if (content_ := self._content) is None:
            self._content = content_ = Content(self)
        return content_

    @property
    def convention(self) -> Convention:
        if (convention_ := self._convention) is None:
            self._convention = convention_ = Convention(self)
        return convention_

    @property
    def genre(self) -> Genre:
        if (genre_ := self._genre) is None:
            self._genre = genre_ = Genre(self)
        return genre_

    # @property
    # def image(self) -> Image:
    #     if(image := self._image) is None:
    #         self._image = image = Image(self.request)
    #     return image

    @property
    def imprint(self) -> Imprint:
        if (imprint_ := self._imprint) is None:
            self._imprint = imprint_ = Imprint(self)
        return imprint_

    # @property
    # def list(self) -> List:
    #     if(list := self._favorite) is None:
    #         self._favorite = list = List(self.request)
    #     return list

    @property
    def parody(self) -> Parody:
        if (parody_ := self._parody) is None:
            self._parody = parody_ = Parody(self)
        return parody_

    @property
    def publisher(self) -> Publisher:
        if (publisher_ := self._publisher) is None:
            self._publisher = publisher_ = Publisher(self)
        return publisher_

    # @property
    # def type(self) -> Type:
    #     if(type_ := self._type) is None:
    #         self._type = type_ = Type(self.request)
    #     return type_

    @property
    def user(self) -> User:
        if (user_ := self._user) is None:
            self._user = user_ = User(self)
        return user_
