from collections import deque

def produce_elements(dq,n):
    for i in range(1,n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            print('Queue full - Yielding control')
            yield

def consume_elements(dq):
    while True:
        while len(dq)>0:
            print('Processing ', dq.pop())
        print('Queue Empty = Yielding control')
        yield

def coordinator():
    dq = deque(maxlen = 10)
    producer = produce_elements(dq, 36)
    consumer = consume_elements(dq)
    while True:
        try:
            print('Producing.....')
            next(producer)
        except StopIteration:
            #Producer finished
            break
        finally:
            print('Consuming....')
            next(consumer)

coordinator()
