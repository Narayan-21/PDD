# Creating a custom sequence with having properties such as concatenation,
# repetition, in-place concatenation, in-place repetition, implementing 
# the reverse multiplication operation and the "in" method.

class Custom:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Custom(name={self.name})'
    def __add__(self, other):
        return Custom(self.name + other.name)
    def __iadd__(self, other):
        if isinstance(other, Custom):
            self.name += other.name
        else:
            self.name += other
        return self
    def __mul__(self, n):
        return Custom(self.name *n)
    def __rmul__(self, n):
        return self.__mul__(n)
    def __imul__(self, n):
        self.name *= n
        return self
    def __contains__(self, value):
        return value in self.name
