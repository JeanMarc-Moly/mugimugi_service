from typing import Iterable, Optional

from fast_enum import FastEnum
from pendulum import parse

from .abstract_paginated import AbstractPaginatedAction
from ..enum import Action, ItemType, Match, ObjectType, SortCriterion, SortOrder, YesNo


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


class SearchObject(AbstractPaginatedAction):
    CONTENT_SEPARATOR = "|"
    CONTENT_ASSOCIATION = ":"

    def __init__(
        self,
        title: Optional[str] = None,
        *,
        page: Optional[int] = None,
        is_adult_only: Optional[bool] = None,
        is_anthology: Optional[bool] = None,
        is_copy_book: Optional[bool] = None,
        is_free: Optional[bool] = None,
        is_censored: Optional[bool] = None,
        match: Optional[str] = None,
        object_type: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
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
        sort_criterion: Optional[str] = None,
        sort_order: Optional[str] = None,
    ):
        super().__init__(page)

        y = YesNo.YES
        n = YesNo.NO

        self.title = None if title is None else str(title)
        self.imprint = None if imprint is None else str(imprint)
        self.publisher = None if publisher is None else str(publisher)
        self.submitter = None if submitter is None else str(submitter)
        self.collection = None if collection is None else str(collection)
        self.convention = None if convention is None else str(convention)
        self.contributor = None if contributor is None else str(contributor)

        self.is_free = None if is_free is None else y if is_free else n
        self.is_censored = None if is_censored is None else y if is_censored else n
        self.is_anthology = None if is_anthology is None else y if is_anthology else n
        self.is_copy_book = None if is_copy_book is None else y if is_copy_book else n
        self.is_adult_only = (
            None if is_adult_only is None else y if is_adult_only else n
        )

        self.genres = None if genres is None else set(genres)
        self.authors = None if authors is None else set(authors)
        self.circles = None if circles is None else set(circles)
        self.contents = None if contents is None else set(contents)
        self.parodies = None if parodies is None else set(parodies)
        self.characters = None if characters is None else set(characters)

        self.date_to = None if date_to is None else parse(date_to)
        self.date_from = None if date_from is None else parse(date_from)

        self.match = None if match is None else Match[match]
        self.sort_order = None if sort_order is None else SortOrder[sort_order]
        self.object_type = None if object_type is None else ObjectType[object_type]
        self.sort_criterion = (
            None if sort_criterion is None else SortCriterion[sort_criterion]
        )

    @staticmethod
    def get_action() -> Action:
        return Action.SEARCH_OBJECT

    @property
    def params(self):
        params = super().params
        p = Parameter

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
            params[p.RELEASE_DATE_FROM.value] = date_from.to_date_string()

        if (date_to := self.date_to) is not None:
            params[p.RELEASE_DATE_TO.value] = date_to.to_date_string()

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

        if (circles := self.circles) :
            t = i.CIRCLE.value
            content += s.join(f"{t}{a}{c}" for c in circles)

        if (authors := self.authors) :
            t = i.AUTHOR.value
            content += s.join(f"{t}{a}{c}" for c in authors)

        if (parodies := self.parodies) :
            t = i.PARODY.value
            content += s.join(f"{t}{a}{c}" for c in parodies)

        if (characters := self.characters) :
            t = i.CHARACTER.value
            content += s.join(f"{t}{a}{c}" for c in characters)

        if (contents := self.contents) :
            t = i.CONTENTS.value
            content += s.join(f"{t}{a}{c}" for c in contents)

        if (genres := self.genres) :
            t = i.GENRE.value
            content += s.join(f"{t}{a}{c}" for c in genres)

        if (convention := self.convention) :
            content += f"{i.CONVENTION.value}{a}{convention}"

        if (collection := self.collection) :
            content += f"{i.COLLECTIONS.value}{a}{collection}"

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
