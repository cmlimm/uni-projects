import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

p = Point(2.34, 5.67)
print ("%.2f" % p.x)
print ("%.2f" % p.y)
point = Point(-18.5, 13.5)
print(point)
