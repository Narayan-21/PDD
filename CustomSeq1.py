from functools import lru_cache
#Edit-11
class Fib:
    def __init__(self, n):
        self.n = n
    def __len__(self):
        # For creating a sequence, a method to define the length of a sequence is a necessity.
        return self.n
    def __getitem__(self, s):
        # s either can be index or can be a slice object.
        # Defining the getitem method for the sequence to grab the item both index-wise as well as through slices.
        if isinstance(s, int): # if s is an integer
            if s<0:
                s= self.n + s
            if s<0 or s>=self.n:
                raise IndexError
                # raising IndexError if the passed value s is either greater than the number of elements in the
                # Fibonacci sequence or if s<0 even after converting it to the positive number to get back to the
                # same element in the sequence by adding n.
            else:
                Fib._fib(s)
        else: # if s is other than integer (slice, range etc..)
            range_tuple = s.indices(self.n)
            print(range_tuple)
    @staticmethod
    @lru_cache(2**10)   # Using lru_cache from functools module to use the memoization technique to reduce the execution time.
    def _fib(n):
        if n<2:
            return 1
        else:
            return Fib._fib(n-1) + Fib._fib(n-2)
            
