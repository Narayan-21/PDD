# A Finite factorial where we give the value of the length of the factorial to
# the instace of Factorials1 class.

import math

class Factorials1:
    def __init__(self, length):
        self.length = length
    def __iter__(self):
        return self.FactIter(self.length)
    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result

# Creating an infinite factorial => So, here we will remove the length argumet of the class.
class Factorials2:
    def __iter__(self):
        return self.FactIter()
    class FactIter:
        def __init__(self):
            self.i = 0
        def __iter__(self):
            return self
        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result
            
