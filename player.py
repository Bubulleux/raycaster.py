from vec2_simple import Vec2
from math import sin, cos
from line import Line


class Player:
    def __init__(self, pos: Vec2):
        self.x = pos._x
        self.y = pos._y
        self.angle = 0
        self.s = sin(self.angle)
        self.c = cos(self.angle)
    
    def update_angle(self, amount):
        self.angle += amount
        self.s = sin(self.angle)
        self.c = cos(self.angle)
    
    def get_ray(self, x):
        return Line(Vec2(self.x+x,self.y), Vec2(self.x+x + 10000*(self.c - self.s), self.y + 10000*(self.s - self.c)))

    def move_forward(self):
        self.x += 0.1
        
    def move_backward(self):
        self.x -= 0.1
        
    def strafe_left(self):
        self.y -= 0.1
    def strafe_right(self):
        self.y += 0.1