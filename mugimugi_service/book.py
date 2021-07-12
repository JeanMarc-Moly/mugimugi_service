from dataclasses import dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import (
    AsyncGenerator,
    AsyncIterable,
    AsyncIterator,
    Iterable,
    Optional,
    Union,
)

from mugimugi_client_api import GetBookById, SearchObject, Vote
from mugimugi_client_api.enum import ObjectType, Score, SortOrder, YesNo
from mugimugi_client_api_entity import Book as Entity
from mugimugi_client_api_entity.root import UpdateRoot
from mugimugi_client_image import Repository

from .abstract_getter import Getter

Path_ = Union[str, Path]
CoverGetter = Union[Iterable[int], AsyncIterable[int]]
CoverSaver = Union[Iterable[tuple[int, Path_]], AsyncIterable[tuple[int, Path_]]]
CoverGot = AsyncIterator[tuple[int, bytes]]
CoverSaved = AsyncIterator[tuple[int, Path]]


class CoverSize(Enum):
    BIG = Repository.COVER_BIG
    SMALL = Repository.COVER_SMALL


@dataclass
class Book(Getter[Entity]):
    @classmethod
    def _get(cls, ids: Iterable[int]) -> GetBookById:
        return GetBookById(ids)

    async def search(
        self,
        title: Optional[str] = None,
        *,
        is_adult_only: Optional[YesNo] = None,
        is_anthology: Optional[YesNo] = None,
        is_copy_book: Optional[YesNo] = None,
        is_free: Optional[YesNo] = None,
        is_censored: Optional[YesNo] = None,
        object_type: Optional[ObjectType] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        circles: Optional[Iterable[str]] = None,
        authors: Optional[Iterable[str]] = None,
        parodies: Optional[Iterable[str]] = None,
        characters: Optional[Iterable[str]] = None,
        contents: Optional[Iterable[str]] = None,
        genres: Optional[Iterable[str]] = None,
        convention: Optional[str] = None,
        collection: Optional[str] = None,
        publisher: Optional[str] = None,
        imprint: Optional[str] = None,
        contributor: Optional[str] = None,
        submitter: Optional[str] = None,
        sort_criterion: Optional[SearchObject.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: int = 0,
    ) -> AsyncGenerator[Entity, None]:
        query = SearchObject(
            title=title,
            is_adult_only=is_adult_only,
            is_anthology=is_anthology,
            is_copy_book=is_copy_book,
            is_free=is_free,
            is_censored=is_censored,
            object_type=object_type,
            date_from=date_from,
            date_to=date_to,
            circles=circles,
            authors=authors,
            parodies=parodies,
            characters=characters,
            contents=contents,
            genres=genres,
            convention=convention,
            collection=collection,
            publisher=publisher,
            imprint=imprint,
            contributor=contributor,
            submitter=submitter,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        ).query_elements
        async with self._api.data as a:
            async for element in query(a):
                yield element
                if not (limit := limit - 1):
                    return

    async def vote(self, score: Score, *ids: int) -> UpdateRoot.Update:
        """
        :raises:
            InvalidScore:  TODO: add log for this one, should not be possible here
            ObjectNotFound:
        """
        async with self._api.data as a:
            async for b in Vote(ids, score).query_bulk_fast(a):
                if not b.is_ok:
                    return False
            else:
                return True

    async def get_covers(
        self,
        entities: Union[Iterable[int], AsyncIterable[int]],
        size: Repository = CoverSize.BIG,
    ) -> AsyncIterator[tuple[int, bytes]]:
        async with self._api.image as a:
            async for c in a.get_many(entities, size.value):
                yield c

    async def save_covers(
        self,
        entities: Union[Iterable[tuple[int, Path_]], AsyncIterable[tuple[int, Path_]]],
        size: Repository = CoverSize.BIG,
    ) -> AsyncIterator[tuple[int, Path]]:
        async with self._api.image as a:
            async for int_path in a.save_many(entities, size.value):
                yield int_path

    async def get_cover(self, entity: int, size: Repository = CoverSize.BIG,) -> bytes:
        return (await self.get_covers([entity], size).__anext__())[1]

    async def save_cover(
        self, entity: int, path: Path_, size: Repository = CoverSize.BIG,
    ) -> Path:
        return (await self.save_covers([(entity, path)], size).__anext__())[1]

    def add(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")

    def edit(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")

    def delete(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")
