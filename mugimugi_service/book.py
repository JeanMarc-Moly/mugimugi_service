from dataclasses import dataclass
from datetime import date
from typing import AsyncGenerator, Iterable, Optional

from mugimugi_client_api import GetBookById, SearchObject, Vote
from mugimugi_client_api.enum import ObjectType, Score, SortOrder, YesNo
from mugimugi_client_api_entity import Book as Entity
from mugimugi_client_api_entity.root import UpdateRoot

from .abstract_getter import Getter


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
        async for element in query(self._api):
            yield element
            if not (limit := limit - 1):
                return

    async def vote(self, score: Score, *ids: int) -> UpdateRoot.Update:
        """
        :raises:
            InvalidScore:  TODO: add log for this one, should not be possible here
            ObjectNotFound:
        """
        async for b in Vote(ids, score).query_bulk_fast(self._api):
            if not b.is_ok:
                return False
        else:
            return True

    def add(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")

    def edit(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")

    def delete(self, **kwargs) -> Entity:
        raise Exception("Not Implemented")
