from datetime import date
from typing import Iterable, Optional

from fast_enum import FastEnum

from ..enum import Action, ItemType, Match, ObjectType, SortOrder, YesNo
from .abstract_paginated import AbstractPaginatedAction


class SearchObject(AbstractPaginatedAction):
    CONTENT_SEPARATOR = "|"
    CONTENT_ASSOCIATION = ":"

    class SortCriterion(metaclass=FastEnum):
        TITLE = "title"
        JAPANESE_TITLE = "jtitle"
        PUBLISHED_DATE = "date"
        PAGES_COUNT = "pages"
        PAGE_VIEWS_COUNT = "page_views"
        SCORE = "score"
        SUBMITTED_DATE = "added"
        LAST_MODIFICATION_DATE = "changed"
        KATAKANA_TITLE = "kana"

    class Parameter(metaclass=FastEnum):

        #   Q=s&
        TITLE = "sn"  # str
        MATCH_TYPE = "match"  # match
        TYPE = "flist"  # object
        RELEASE_DATE_FROM = "date"  # str YYYY-MM-DD
        RELEASE_DATE_TO = "date2"  # str YYYY-MM-DD

        CONTRIBUTOR = "cont"
        SUBMITTER = "sub"
        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

        IS_ADULT_ONLY = "age"  # yes_no
        IS_ANTHOLOGY = "anth"  # yes_no
        IS_COPY_BOOK = "bcopy"  # yes_no
        IS_FREE = "FREE"  # yes_no
        IS_CENSORED = "scen"  # yes_no

        # Regroup several parameters of the HTML API:
        # - SLIST_CIRCLE,
        # - SLIST_AUTHOR,
        # - SLIST_PARODY,
        # - SLIST_CHAR,
        # - SLIST_CONTENT,
        # - SLIST_GENRE,
        # - SLIST_CONVE,
        # - SLIST_COLL
        # - SLIST_PUBL
        # - SLIST_IMPRINT
        # Will have to include ItemType as prefix of each element
        # All elements are pipe separated.
        # ex: &slist=C:Electro|K:Swimsuit|P:Moetan
        CONTENT = "slist"

    def __init__(
        self,
        title: Optional[str] = None,
        *,
        page: Optional[int] = None,
        is_adult_only: Optional[YesNo] = None,
        is_anthology: Optional[YesNo] = None,
        is_copy_book: Optional[YesNo] = None,
        is_free: Optional[YesNo] = None,
        is_censored: Optional[YesNo] = None,
        match: Optional[Match] = None,
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
        sort_criterion: Optional[SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ):
        super().__init__(page)

        self.title = title
        self.imprint = imprint
        self.publisher = publisher
        self.submitter = submitter
        self.collection = collection
        self.convention = convention
        self.contributor = contributor

        self.is_free = is_free
        self.is_censored = is_censored
        self.is_anthology = is_anthology
        self.is_copy_book = is_copy_book
        self.is_adult_only = is_adult_only

        self.genres = genres
        self.authors = authors
        self.circles = circles
        self.contents = contents
        self.parodies = parodies
        self.characters = characters

        self.date_to = date_to
        self.date_from = date_from

        self.match = match
        self.sort_order = sort_order
        self.object_type = object_type
        self.sort_criterion = sort_criterion

    @staticmethod
    def get_action() -> Action:
        return Action.SEARCH_OBJECT

    @property
    def params(self) -> dict[str, str]:
        params = super().params
        p = self.Parameter

        if (title := self.title) is not None:
            params[p.TITLE.value] = title

        if (match := self.match) is not None:
            params[p.MATCH_TYPE.value] = match.value

        if (is_adult_only := self.is_adult_only) is not None:
            params[p.IS_ADULT_ONLY.value] = is_adult_only.value

        if (is_anthology := self.is_anthology) is not None:
            params[p.IS_ANTHOLOGY.value] = is_anthology.value

        if (is_copy_book := self.is_copy_book) is not None:
            params[p.IS_COPY_BOOK.value] = is_copy_book.value

        if (is_free := self.is_free) is not None:
            params[p.IS_FREE.value] = is_free.value

        if (object_type := self.object_type) is not None:
            params[p.TYPE.value] = object_type.value

        if (date_from := self.date_from) is not None:
            params[p.RELEASE_DATE_FROM.value] = f"{date_from:%Y-%m-%d}"

        if (date_to := self.date_to) is not None:
            params[p.RELEASE_DATE_TO.value] = f"{date_to:%Y-%m-%d}"

        if (sort_criterion := self.sort_criterion) is not None:
            params[p.SORT_CRITERION.value] = sort_criterion.value

        if (sort_order := self.sort_order) is not None:
            params[p.SORT_ORDER.value] = sort_order.value

        if (is_censored := self.is_censored) is not None:
            params[p.IS_CENSORED.value] = is_censored.value

        a = self.CONTENT_ASSOCIATION
        s = self.CONTENT_SEPARATOR
        i = ItemType
        content = ""

        if (circles := self.circles) and (circles := set(circles)):
            t = i.CIRCLE.value
            content += s.join(f"{t}{a}{c}" for c in circles)

        if (authors := self.authors) and (authors := set(authors)):
            t = i.AUTHOR.value
            content += s.join(f"{t}{a}{c}" for c in authors)

        if (parodies := self.parodies) and (parodies := set(parodies)):
            t = i.PARODY.value
            content += s.join(f"{t}{a}{c}" for c in parodies)

        if (characters := self.characters) and (characters := set(characters)):
            t = i.CHARACTER.value
            content += s.join(f"{t}{a}{c}" for c in characters)

        if (contents := self.contents) and (contents := set(contents)):
            t = i.CONTENT.value
            content += s.join(f"{t}{a}{c}" for c in contents)

        if (genres := self.genres) and (genres := set(genres)):
            t = i.GENRE.value
            content += s.join(f"{t}{a}{c}" for c in genres)

        if (convention := self.convention) :
            content += f"{i.CONVENTION.value}{a}{convention}"

        if (collection := self.collection) :
            content += f"{i.COLLECTION.value}{a}{collection}"

        if (publisher := self.publisher) :
            content += f"{i.PUBLISHER.value}{a}{publisher}"

        if (imprint := self.imprint) :
            content += f"{i.IMPRINT.value}{a}{imprint}"

        if (contributor := self.contributor) :
            content += f"{i.CONTRIBUTOR.value}{a}{contributor}"

        if (submitter := self.submitter) is not None:
            content += f"{i.SUBMITTER.value}{a}{submitter}"

        if content:
            params[p.CONTENT.value] = content

        return params
