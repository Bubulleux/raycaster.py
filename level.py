from line import Line
from vec2_simple import Vec2

class Wall:
    def __init__(self, p1: Vec2,p2: Vec2 , color):
        self.p = Line(p1, p2)
        self.c = color
    def get_color(self):
        return self.c
    def get_pos(self):
        return self.p
    def distance(self, p: Vec2):
        return self.p.distance(p)
    
    
    def __str__(self):
        return str(self.c)

class Level:
    def __init__(self, walls: tuple, pos: tuple):
        self.walls = walls
        self.init_pos = pos