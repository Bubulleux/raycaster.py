from vec2_simple import Vec2
from math import log2
from time import perf_counter

p_temp = Vec2(0,0)

def clamp(x: float):
    """Limit a position to an area."""
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x

def clamp_full(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x
    

class Line():
    def __init__(self, pos1: Vec2, pos2: Vec2):
        """
        pos1 origin
        pos2 NORMALIZED direction
        """
        self.x1 = pos1._x
        self.y1 = pos1._y
        self.x2 = pos2._x
        self.y2 = pos2._y
        
    def distance(self, p: Vec2):
        ba, pa = Vec2(self.x2 - self.x1, self.y2 - self.y1), Vec2(p._x - self.x1, p._x - self.y1)
        return (pa - ba * clamp(pa.dot(ba)/ba.dot(ba))).length()
    
    def mid(self):
        return self.a*0.5 + self.b*0.5
    
    def dot(self, p: Vec2):
        return self.mid().dot(p)
        
    def intersect(self, line: 'Line'):
        
        i = 1/((self.x1 - self.x2) * (line.y1 - line.y2) - (self.y1 - self.y2) * (line.x1 - line.x2))
        t, u = i * ((self.x1 - line.x1) * (line.y1 - line.y2) - (self.y1 - line.y1) * (line.x1 - line.x2)), \
               i * ((self.x1 - line.x1) * (self.y1 - self.y2) - (self.y1 - line.y1) * (self.x1 - self.x2)) 
        
        if t >= 0 and t <=1 and u >= 0 and u <=1:
            return Vec2(self.x1  + t * (self.x2 - self.x1), self.y1 + t * (self.y2 - self.y1))
        return
    
    def ray_line_intersect(self, line: 'Line'):
        v2 = line.b - line.a
        return self.a + self.b * ((v2 * (self.a - line.a)).length() / v2.dot(Vec2(-self.y2, self.x2)))

    def put_on_screen(self, line: 'Line', height):
        p_temp = self.intersect(line)
        if p_temp == None:
            return
        return int(height-clamp_full(height -(self.distance(p_temp)*10), 0, height))>>1

if __name__ == '__main__':
    origin = Vec2(0,0)
    l1 = Line(Vec2(0,0), Vec2(1000000,1000000))
    l2 = Line(Vec2(1,0), Vec2(0,1))
    line_count = 24 * 100
    t1 = perf_counter()
    for i in range(line_count):
        it = origin.distance(l1.intersect(l2))
        #it = origin.distance(l1.ray_line_intersect(l2))
    t2 = perf_counter()
    print(it, t2-t1)
    t1 = perf_counter()
    for i in range(24):
        it = l2.distance(origin)
    t2 = perf_counter()
    print(it, t2-t1)
    t1 = perf_counter()
    l=[Vec2(100000+i,100000+i) for i in range(100)]
    t2 = perf_counter()
    print(t2-t1)
    