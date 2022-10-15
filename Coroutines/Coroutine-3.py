# Using decorator to prime the coroutine.
from inspect import getgeneratorstate
import math


def coroutine(gen_fn):
    def prime(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return prime

@coroutine
def echo():
    while True:
        received = yield
        print(received)

e=echo()
e.send('Hello')
print(getgeneratorstate(e))


@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        try:
            result = math.pow(received, p)
        except TypeError:
            result = None

squares = power_up(2)
cubes = power_up(3)
print(squares.send(4))
print(cubes.send(9))
print(getgeneratorstate(squares))
squares.close()
print(getgeneratorstate(squares))
