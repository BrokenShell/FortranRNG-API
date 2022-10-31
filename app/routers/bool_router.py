from fastapi import APIRouter
import FortranRNG

Router = APIRouter(tags=["Random Boolean"])


@Router.get("/percent-true")
async def percent_true(percent: float):
    """<pre><code>Linear distribution
    Zero or less is always False
    One hundred or more is always True
    @param percent: Float [0.0, 100.0], represents the percent of true in the distribution
    @return: Random Boolean</pre></code>"""
    return FortranRNG.percent_true(percent) == 1
