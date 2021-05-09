from asyncio import run
from contextlib import suppress
from dataclasses import dataclass
from datetime import date
from typing import Coroutine, Iterable, Iterator, Optional

from ..action import GetBookById, SearchObject, Vote
from ..entity.main import Book as Entity
from ..entity.root import UpdateRoot
from ..enum import ObjectType, Score, SortOrder, YesNo
from .abstract import AbstractService
from .abstract_getter import Getter


@dataclass
class Book(AbstractService, Getter[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetBookById:
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
        limit: Optional[int] = 0,
    ) -> Iterator[Entity]:
        with suppress(StopIteration):
            parse = self.CONSTRUCTOR.parse
            pages = self.search_pages(
                title,
                is_adult_only,
                is_anthology,
                is_copy_book,
                is_free,
                is_censored,
                object_type,
                date_from,
                date_to,
                circles,
                authors,
                parodies,
                characters,
                contents,
                genres,
                convention,
                collection,
                publisher,
                imprint,
                contributor,
                submitter,
                sort_criterion,
                sort_order,
            )
            page = None
            while page := pages.send(page):
                page = parse(await page)
                for element in page.elements:
                    yield element
                    if not (limit := limit - 1):
                        return

    def search_(
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
        limit: Optional[int] = 0,
    ) -> Iterator[Entity]:
        with suppress(StopIteration):
            parse = self.CONSTRUCTOR.parse
            pages = self.search_pages(
                title,
                is_adult_only,
                is_anthology,
                is_copy_book,
                is_free,
                is_censored,
                object_type,
                date_from,
                date_to,
                circles,
                authors,
                parodies,
                characters,
                contents,
                genres,
                convention,
                collection,
                publisher,
                imprint,
                contributor,
                submitter,
                sort_criterion,
                sort_order,
            )
            page = None
            while page := pages.send(page):
                page = parse(run(page))
                for element in page.elements:
                    yield element
                    if not (limit := limit - 1):
                        return

    def search_pages(
        self,
        title: Optional[str] = None,
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
    ) -> Iterator[Coroutine]:
        action = iter(
            SearchObject(
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
            )
        )
        query = self._api.query
        response = None
        with suppress(StopIteration):
            while paginated_action := action.send(response):
                response = yield query(paginated_action)

    async def vote(self, score: Score, *ids: int) -> UpdateRoot.Update:
        """
        :raises:
            InvalidScore:  TODO: add log for this one, should not be possible here
            ObjectNotFound:
        """
        # can't use 'all' TT
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
