from ...action import SearchObject as Action
from .abstract_paginated import AsynchronousPaginatedClient


class SearchObject(AsynchronousPaginatedClient, Action):
    ...
