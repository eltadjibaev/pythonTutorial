
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')
    
    def draw(self):
        print('draw')

p1 = Point(5, 7)
p1.draw()

p2 = Point(10, 20)
