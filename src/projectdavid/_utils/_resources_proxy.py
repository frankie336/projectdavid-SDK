from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `projectdavid.resources` module.

    This is used so that we can lazily import `projectdavid.resources` only when
    needed *and* so that users can just import `projectdavid` and reference `projectdavid.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("projectdavid.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
