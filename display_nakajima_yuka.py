#!.python_env/bin/python
from asyncio import run

from mugimugi.client.synchronous import SearchObject as SyncSearchObject
from mugimugi.client.asynchronous import SearchObject as AsyncSearchObject


async def displayAsync():
    query = AsyncSearchObject(
        authors=["Nakajima Yuka"],
        match="EXACT",
        sort_criterion="PUBLISHED_DATE",
        sort_order="DESCENDING",
    )
    async for e in query.fetch_all_elements():
        print(e.tag, e.attrib)
        print(e.items())


def displaySync():
    query = SyncSearchObject(
        authors=["Nakajima Yuka"],
        match="EXACT",
        sort_criterion="PUBLISHED_DATE",
        sort_order="DESCENDING",
    )
    for e in query.fetch_all_elements():
        print(e.tag, e.attrib)
        print(e.items())


displaySync()
# run(displayAsync())
