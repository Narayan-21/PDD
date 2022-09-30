from contextlib import contextmanager

@contextmanager
def open_file(fname):
    print(f'opening {fname}')
    f= open(fname)
    try:
        yield f
    finally:
        print(f'closing {fname}')
        f.close()

class NestedContexts:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self
    
    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value
    
    def __exit__(self, typ, val, tb):
        for exit in self._exits[::-1]:
            exit(typ,val,tb)
        return False

fnames = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f)) for f in fnames]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

# Another Example
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f)) for f in fnames]
    print('Do work')
