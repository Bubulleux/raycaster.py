from math import sqrt, sin, cos
class Vec2:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def distance(a: 'Vec2', b: 'Vec2'):
        return sqrt((b._x - a._x) * (b._x - a._x) + (b._y - a._y) * (b._y - a._y) )
    def length(self):
        return sqrt(self._x*self._x + self._y*self._y)
    def rotate(self, angle):
        self._x, self._y = 
    def dot(self, a: 'Vec2'):
        return self._x*a._x+self._y*a._y
    def __add__(self, other: 'Vec2'):
        return Vec2(self._x+other._x, self._y+other._y)
    def __sub__(self, other: 'Vec2'):
        return Vec2(self._x-other._x, self._y-other._y)
    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self._x*other._y, -self._y*other._x)
        return Vec2(self._x*other, self._y*other)