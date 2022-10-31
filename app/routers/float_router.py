from fastapi import APIRouter
import FortranRNG

Router = APIRouter(tags=["Random Float"])


@Router.get("/canonical")
async def canonical():
    """<pre><code>Flat uniform distribution
    @return: Random Float in range `[0.0, 1.0)`</pre></code>"""
    return FortranRNG.canonical()


@Router.get("/random-float")
async def random_float(low: float, high: float):
    """<pre><code>Flat uniform distribution
    @param low: Float
    @param high: Float
    @return: Random Float in range `[low, high)`</pre></code>"""
    return FortranRNG.random_float(low, high)


@Router.get("/triangular")
async def triangular(low: float, high: float, mode: float):
    """<pre><code>Linear distribution about the mode
    @param low: Float
    @param high: Float
    @param mode: Float
    @return: Random Float in range `[low, high]`</pre></code>"""
    return FortranRNG.triangular(low, high, mode)
