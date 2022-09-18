import math
#Goal-1_2
class Point:
    def __init__(self, x,y):
        self._pt = (x,y)
    def __repr__(self):
        return f'A 2-dimensional point: Point({self._pt[0]},{self._pt[1]})'
    def __len__(self):
        return len(self._pt)
    def __getitem__(self, s):
        return self._pts[s]

class Polygon:
    def __init__(self, *pts):
        self._pts = [Point(*pt) for pt in pts]
        if len(self._pts)<3:
            raise ValueError('Minimum number of points for a polygon is 3')
    def __repr__(self):
        return f'Polygon with a total number of {len(self._pts)} vertices. The co-ordinates of these vertices are ({[str(pt) for pt in self._pts]})'
    @property
    def distance(self):
        return math.sqrt((self._pts[0][0]-self._pts[1][0])**2 + (self._pts[0][1]-self._pts[1][1])**2)
    @property
    def distance2(self):
        return math.sqrt((self._pts[1][0]-self._pts[2][0])**2 + (self._pts[1][1]-self._pts[2][1])**2)
    @property
    def distance3(self):
        return math.sqrt((self._pts[0][0]-self._pts[2][0])**2 + (self._pts[0][1]-self._pts[2][1])**2)
    @property
    def circumrad(self):
        return (self.distance)/((2)*(math.sin(math.pi/len(self._pts))))
    @property
    def angle(self):
        return (len(self._pts)-2)*(math.pi/len(self._pts))
    @property
    def apothem(self):
        return (self.distance)/2*(math.tan(180/len(self._pts)))
    @property
    def area(self):
        return (len(self._pts)*(self.distance)*(self.apothem))/2
    @property
    def perimeter(self):
        return len(self._pts)*(self.distance)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (len(self._pts) == len(other._pts)
                    and self.circumrad == other.circumrad)
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return len(self._pts) > len(other._pts)
        else:
            return NotImplemented
