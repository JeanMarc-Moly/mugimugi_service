from datetime import date
from typing import Optional

from fast_enum import FastEnum

from ..enum import Action, SortOrder
from .abstract_paginated import AbstractPaginatedAction


class SearchItem(AbstractPaginatedAction):
    CONTENT_SEPARATOR = "|"
    CONTENT_ASSOCIATION = ":"

    class SortCriterion(metaclass=FastEnum):
        TITLE = "title"
        JAPANESE_TITLE = "jtitle"
        OBJECTS = "objects"
        LAST_MODIFICATION_DATE = "changed"

    class Type(metaclass=FastEnum):
        CIRCLE = "circle"
        AUTHOR = "author"
        PARODY = "parody"
        CHARACTER = "character"
        CONTENT = "contents"
        GENRE = "genre"
        CONVENTION = "convention"
        COLLECTION = "collections"
        PUBLISHER = "publisher"
        IMPRINT = "imprint"

    class Parameter(metaclass=FastEnum):
        TITLE = "sn"  # str
        TYPE = "T"  # Type

        DATE = "date"  # str YYYY-MM-DD, limited to convention
        CONTRIBUTOR = "cont"  # str

        SORT_CRITERION = "order"  # SortCriterion
        SORT_ORDER = "flow"  # SortOrder

    def __init__(
        self,
        title: str,
        type_: Type,
        *,
        page: Optional[int] = None,
        date_: Optional[date] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ):
        super().__init__(page)

        self.title = title
        self.type_ = type_

        self.date_ = date_
        self.contributor = contributor

        self.sort_order = sort_order
        self.sort_criterion = sort_criterion

    @staticmethod
    def get_action() -> Action:
        return Action.SEARCH_ITEM

    @property
    def params(self) -> dict[str, str]:
        params = super().params
        p = self.Parameter

        if (title := self.title) is not None:
            params[p.TITLE.value] = title

        if (type_ := self.type_) is not None:
            params[p.TYPE.value] = type_.value

        if (date_ := self.date_) is not None:
            params[p.DATE.value] = f"{date_:%Y-%m-%d}"

        if (contributor := self.contributor) is not None:
            params[p.CONTRIBUTOR.value] = contributor

        if (sort_criterion := self.sort_criterion) is not None:
            params[p.SORT_CRITERION.value] = sort_criterion.value

        if (sort_order := self.sort_order) is not None:
            params[p.SORT_ORDER.value] = sort_order.value

        return params
