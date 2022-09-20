#Creating a Circle class while practicing Lazy iterables.

import math

class Circle:
    def __init__(self,r):
        self.radius = r
        self._area = None
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,r):
        self._radius = r
        self._area = None
    @property
    def area(self):
        if self._area is None:
            print('Calculating Area....')
            self._area = math.pi * (self.radius**2)
        return self._area
