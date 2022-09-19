import math

class Polygon:
    def __init__(self, n, r):
        if n<3:
            raise ValueError('Polygon must have atleast three sides/vertices')
        self.n = n
        self.r = r
    def __repr__(self):
        return f'Polygon with a total number of {self.n} vertices and with the circumradius of {self.r}'

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
        return (2*self.r)*(math.sin(math.pi/self.n))
    @property
    def angle(self):
        return (self.n-2)*(math.pi/self.n)
    @property
    def apothem(self):
        return self.r*(math.cos(math.pi/self.n))
    @property
    def area(self):
        return (self.n*self.edge*self.apothem)/2
    @property
    def perimeter(self):
        return self.n*self.edge
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
        
class Polygons:
    def __init__(self,m,r):
        if m<3:
            raise ValueError('m must be greater than 3')
        self.m = m
        self.r = r
        self.polygons = [Polygon(i,r) for i in range(3,m+1)]
    def __len__(self):
        return self.m-2
    def __repr__(self):
        return f'Polygons(m={self.m}, r= {self.r})'
    def __getitem__(self,s):
        return self.polygons[s]
    @property
    def max_eff_poly(self):
        sorted_poly = sorted(self.polygons,
                             key=lambda p: p.area/p.perimeter,
                             reverse=True)
        return sorted_poly[0]
