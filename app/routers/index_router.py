from fastapi import APIRouter
import FortranRNG

Router = APIRouter(tags=["Random Index"])


@Router.get("/random-index")
async def random_index(limit: int):
    """<pre><code>Flat uniform distribution
    @param limit: Integer
    @return: Random Integer in range `[0, limit) or [limit, 0) for limit < 0`</pre></code>"""
    return FortranRNG.random_index(limit)


@Router.get("/front-linear")
async def front_linear(limit: int):
    """<pre><code>Front linear distribution
    @param limit: Integer
    @return: Random Integer in range `[0, limit) or [limit, 0) for limit < 0`</pre></code>"""
    return FortranRNG.front_linear(limit)


@Router.get("/back-linear")
async def back_linear(limit: int):
    """<pre><code>Back linear distribution
    @param limit: Integer
    @return: Random Integer in range `[0, limit) or [limit, 0) for limit < 0`</pre></code>"""
    return FortranRNG.back_linear(limit)
