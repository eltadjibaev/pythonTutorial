import classes
from classes import Point

p = Point(3, 4)
p.move()

import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob']
print(random.choice(members))