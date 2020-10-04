from abc import abstractmethod

from .abstract import Client
from ..action.abstract_paginated import Parameter


class PaginatedClient(Client):
    PAGE = Parameter.PAGE.value

    # Contrary to doc, returns up to 50 elements, not 25 (+1 for user).
    MIN_PER_PAGE = 1
    MAX_PER_PAGE = 50 + 1

    @abstractmethod
    def fetch_all_elements(self, **kwargs):
        ...

    @abstractmethod
    def fetch_all(self, **kwargs):
        ...
