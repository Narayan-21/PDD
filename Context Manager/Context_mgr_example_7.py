# Using contextmanager from contextlib module
from contextlib import contextmanager
from time import perf_counter, sleep

# Example-1

@contextmanager
def open_file(fname, mode='r'):
    print('Opening File...')
    f=open(fname, mode)
    try:
        yield f
    finally:
        print('Closing File...')
        f.close()

with open_file('test.txt','r') as f:
    print(f.readlines())


# Example-2
@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['Start']=start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end']=end
        stats['elapsed']=end-start

with timer() as sts:
    sleep(3)

print(sts)
