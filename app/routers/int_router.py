from fastapi import APIRouter
import FortranRNG

Router = APIRouter(tags=["Random Integer"])


@Router.get("/d")
async def d(sides: int):
    """<pre><code>Flat uniform distribution
    @param sides: Integer
    @return: Random Integer in range `[1, sides]`</pre></code>"""
    return FortranRNG.d(sides)


@Router.get("/dice")
async def dice(rolls: int, sides: int):
    """<pre><code>Geometric distribution based on the number and size of the dice rolled
    @param rolls: Integer, number of times to roll the die
    @param sides: Integer, die size or number of sides, most commonly six
    @return: Random Integer in range `[X, Y]` where X = rolls and Y = rolls * sides</pre></code>"""
    return FortranRNG.dice(rolls, sides)


@Router.get("/random-below")
def random_below(stop: int):
    """<pre><code>Flat uniform distribution, tail exclusive
    @param stop: Integer, represents the upper bound
    @return: Random Integer in range `[0, stop)`</pre></code>"""
    return FortranRNG.random_below(stop)


@Router.get("/random-integer")
def random_integer(low: int, high: int):
    """<pre><code>Flat uniform distribution, inclusive
    @param low: Integer
    @param high: Integer
    @return: random integer in range `[low, high]`</pre></code>"""
    return FortranRNG.random_integer(low, high)


@Router.get("/random-range")
def random_range(start: int, stop: int, step: int):
    """<pre><code>Flat uniform distribution, tail exclusive
    @param start: Integer
    @param stop: Integer
    @param step: Integer
    @return: Random Integer in range `[start, stop)` by increments of step</pre></code>"""
    return FortranRNG.random_range(start, stop, step)


@Router.get("/plus-or-minus")
def plus_or_minus(amount):
    """<pre><code>Flat uniform distribution
    @param amount: Integer
    @return: Random Integer in range `[-amount, amount]`</pre></code>"""
    return FortranRNG.plus_or_minus(amount)


@Router.get("/plus-or-minus-linear")
def plus_or_minus_linear(amount):
    """<pre><code>Geometric linear distribution, centered on zero
    @param amount: Integer
    @return: Random Integer in range `[-amount, amount]`</pre></code>"""
    return FortranRNG.plus_or_minus_linear(amount)
