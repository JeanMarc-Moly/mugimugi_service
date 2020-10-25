from ...action import SearchItem as Action
from .abstract_paginated import AsynchronousPaginatedClient


class SearchItem(AsynchronousPaginatedClient, Action):
    ...
