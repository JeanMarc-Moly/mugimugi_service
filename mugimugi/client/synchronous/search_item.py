from ...action import SearchItem as Action
from .abstract_paginated import SynchronousPaginatedClient


class SearchItem(SynchronousPaginatedClient, Action):
    ...
