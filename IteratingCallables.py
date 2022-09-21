# Creating a CallableIterator Class that can be used to iterate over the return values of the callables.

class CallableIterator:
    def __init__(self, callable_, sentinel):
        self.callable_ = callable_
        self.sentinel = sentinel
        self.is_consumed = False
    def __iter__(self):
        return self
    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self.callable_()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result
