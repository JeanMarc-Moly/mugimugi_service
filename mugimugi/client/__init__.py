from typing import ClassVar
from contextlib import suppress

from httpx import AsyncClient, Response, codes
from httpx._types import QueryParamTypes

from ..configuration import API_PATH
from ..entity.root import FailedRoot


class Client:
    API: ClassVar[str] = API_PATH

    def __init__(self, key: str) -> None:
        self.api = self.API.format(key=key)

    async def query(self, params: QueryParamTypes) -> str:
        """
        params: anything with "items" method
        """
        async with AsyncClient() as client:
            return self._parse(await client.get(self.api, params=params, timeout=None))

    @staticmethod
    def _parse(r: Response) -> str:
        content = r.text
        # print(content)
        if (status := r.status_code) != codes.OK:
            raise Exception(f"Error {codes(status)} ({status}): {content}")

        with suppress(TypeError):
            FailedRoot.parse(content).error.blow()

        return content
