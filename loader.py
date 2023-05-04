from level import Wall
from vec2_simple import Vec2

def load_level(name):
    f = open('levels\\'+name+'.txt', 'r')
    s = f.read()
    l=[0,0,0,0,0]
    temp= ''
    i = 0
    level = []
    for c in s:
        print(c)
        if c == ';':
            if i <= 3:
                l[i] = float(temp)
                i += 1
            else:
                l[4] = int(temp)
                level.append(Wall(Vec2(l[0], l[1]), Vec2(l[2], l[3]), l[4]))
                i=0
            temp=''
        else:
            temp += c
    return level
            
print(load_level('1'))