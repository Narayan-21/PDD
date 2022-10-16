# Creating a coroutine(echo()) while practicing the Exception propagation
# between the subgenerator, delegator and the caller.

class IgnoreMe(Exception):
    pass

class CloseCoroutine(Exception):
    pass

def delegator():
    result = yield from echo()
    yield 'Subgen closed and returned:', result
    print('Delegator Closing...')

def echo():
    output = None
    try:
        while True:
            try:
                received = yield output
                print(received)
            except IgnoreMe:
                output = "I'm ignoring you!"
            else:
                output = None
    except CloseCoroutine:
        return 'Coroutine was closed'
    except GeneratorExit:
        print('Closed method was called/ or GeneratorExit thrown')
        return 'From a GeneratorExit'
    
d= delegator()
next(d)
d.send('Python')
print(d.throw(IgnoreMe))
d.send('Rocks!!')
