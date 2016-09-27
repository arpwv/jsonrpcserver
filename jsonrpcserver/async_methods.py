"""Python 3.5+ users can dispatch requests to coroutines.

Usage is the same as before, but this time import from ``jsonrpcserver.aio``::

    from jsonrpcserver.aio import methods

    @methods.add
    async def ping():
        return await some_long_running_task()

Then ``await`` the dispatch::

    await methods.dispatch(request)
"""
from .methods import Methods
from .async_dispatcher import dispatch

class AsyncMethods(Methods):

    async def dispatch(self, request):
        return await dispatch(self, request)

    def serve_forever(self):
        raise NotImplementedError()
