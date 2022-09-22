import math

class Polygon:
    def __init__(self, n, r):
        if n<3:
            raise ValueError('Polygon must have atleast three sides/vertices')
        self.n = n
        self.r = r
        self._int_angle = None
        self._side_len = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        
    def __repr__(self):
        return f'Polygon(n={self.n}, r= {self.r})'

    @property
    def vertices(self):
        return self.n
    
    @property
    def n_edges(self):
        return self.n
    
    @property
    def c_radius(self):
        return self.r
    
    @property
    def edge(self):
        if self._side_len is None:
            self._side_len = (2*self.r)*(math.sin(math.pi/self.n))
        return self._side_len
    
    @property
    def angle(self):
        if self._int_angle is None:
            self._int_angle = (self.n-2)*(180/self.n)
        return self._int_angle
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.r*(math.cos(math.pi/self.n))
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = (self.n*self.edge*self.apothem)/2
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.n*self.edge
        return self._perimeter
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.n_edges == other.n_edges
                    and self.c_radius == other.c_radius)
        else:
            return NotImplemented
        
    def __gt__(self,other):
        if isinstace(other, Polygon):
            return self.vertices > other.vertices
        else:
            return NotImplemented

    
