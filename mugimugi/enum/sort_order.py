from __future__ import annotations

from fast_enum import FastEnum


class SortOrder(metaclass=FastEnum):
    ASCENDING = "ASC"
    DESCENDING = "DESC"
