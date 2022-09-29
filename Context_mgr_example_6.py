# Using Decoraotrs to create context manager using generator functions.

class GenContextManager:
    def __init__(self,gen):
        self.gen = gen
    def __enter__(self):
        print('Calling next to get the yielded value from the generator')
        return next(self.gen)
    def __exit__(self, typ, val, tb):
        print('Calling next to perform cleanup in generator')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False
    
def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

@context_manager_dec
def open_file(fname, mode='r'):
    print('Opening File...')
    f= open(fname, mode)
    try:
        yield f
    finally:
        print('Closing File...')
        f.close()

with open_file('test.txt') as f:
    print(f.readlines())
