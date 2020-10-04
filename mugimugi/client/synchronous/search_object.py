from ...action import SearchObject as Action
from .abstract_paginated import SynchronousPaginatedClient


class SearchObject(SynchronousPaginatedClient, Action):
    ...
