from httpx import get

from ..abstract import Client


class SynchronousClient(Client):
    def query(self, **kwargs):
        return self._query({**self.params, **kwargs})

    @classmethod
    def _query(cls, params: dict):
        return cls._parse(get(cls.API, params=params, timeout=None))
