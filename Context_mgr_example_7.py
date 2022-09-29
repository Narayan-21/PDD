# Using contextmanager from contextlib module
from contextlib import contextmanager

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
