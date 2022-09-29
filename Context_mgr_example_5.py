# Creating a Context Manager using generator function

class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)
    def __enter__(self):
        return next(self._gen)
    def __exit__(self, typ, val, tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname, mode):
    f= open(fname, mode)
    try:
        print('Opening file....')
        yield f
    finally:
        print('Closing file....')
        f.close()
