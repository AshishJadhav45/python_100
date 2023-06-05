# write a program to calculate to arclenth claim to angle by assigning values to the radius and angles

# formula 2 * pi * randius * angle/360

import math 
class Arclenth:
    def __init__ (self):
        self.radius = 0
        self.angle = 0

    def calculate_arc_length(self):
        result = 2 * math.pi * self.radius*self.angle/360
        print(f"length of an arc is {result}")
a1 = Arclenth()
a1.radius = 9
a1.angle = 75
print(f"Angle is {a1.angle}")
print(f"radious is {a1.radius}")
a1.calculate_arc_length()