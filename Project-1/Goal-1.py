import math

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
    def __repr__(self):
        return f'Polygon with a total number of {len(self._pts)} vertices. The co-ordinates of these vertices are ({[str(pt) for pt in self._pts]})'
    def distance(self):
        self.distance = math.sqrt((self._pts[0][0]-self._pts[1][0])**2 + (self._pts[0][1]-self._pts[1][1])**2))
    def circumRad(self):
        self.cr = (self.distance)/((2)*(math.sin(math.pi/len(self._pts))))
    def angle(self):
        self.angle = (len(self._pts)-2)*(math.pi/len(self._pts))
    def 
