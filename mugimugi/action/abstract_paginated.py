from abc import abstractstaticmethod
from fast_enum import FastEnum

from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    PAGE = "page"  # int > 0


class AbstractPaginatedAction(AbstractAction):
    page: int

    def __init__(self, page: int) -> None:
        if page:
            page = int(page)
        if not page or page < 1:
            page = 1
        self.page = page

    @property
    def params(self):
        params = super().params
        params[Parameter.PAGE.value] = self.page
        return params 
        