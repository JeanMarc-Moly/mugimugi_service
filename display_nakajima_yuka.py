#!.python_env/bin/python
# from asyncio import run

from mugimugi.enum import Match, SortOrder
from mugimugi.client.synchronous import SearchObject as SyncSearchObject
from mugimugi.client.asynchronous import SearchObject as AsyncSearchObject


async def displayAsync():
    query = AsyncSearchObject(
        authors=["Nakajima Yuka"],
        match=Match.EXACT,
        sort_criterion=AsyncSearchObject.SortCriterion.PUBLISHED_DATE,
        sort_order=SortOrder.DESCENDING,
    )
    async for e in query.fetch_all_elements():
        print(e.tag, e.attrib)
        print(e.items())


def displaySync():
    query = SyncSearchObject(
        authors=["Nakajima Yuka"],
        match=Match.EXACT,
        sort_criterion=SyncSearchObject.SortCriterion.PUBLISHED_DATE,
        sort_order=SortOrder.DESCENDING,
    )
    for e in query.fetch_all_elements():
        print(e.tag, e.attrib)
        print(e.items())


displaySync()
# run(displayAsync())
