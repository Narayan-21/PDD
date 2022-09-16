# Creating a Three dimensional point class as a sequence with methods
# such as __getitem__ and __len__ etc.

import numbers

class Point:
    def __init__(self, x, y,z):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real) and isinstance(z, numbers.Real):
            self._pt = (x,y,z)
        else:
            raise TypeError('Point co-ordinate must be a real number')
    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]}, z={self._pt[2]})'
    def __len__(self):
        return len(self._pt)
    def __getitem__(self, s):
        return self._pt[s]
