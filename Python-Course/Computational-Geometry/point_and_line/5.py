import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.a > 0:
            str_a = '{:.2f}'.format(self.a)
        else:
            str_a = '-{:.2f}'.format(abs(self.a))

        if self.b > 0:
            str_b = '+ {:.2f}'.format(self.b)
        else:
            str_b = '- {:.2f}'.format(abs(self.b))

        if self.c > 0:
            str_c = '+ {:.2f}'.format(self.c)
        else:
            str_c = '- {:.2f}'.format(abs(self.c))

        return '{}x {}y {} = 0'.format(str_a, str_b, str_c)

    def distanceToZero(self):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return abs(self.c)/denominator
        else:
            return 0

    def distanceToPoint(self, point):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return abs(self.a*point.x + self.b*point.y + self.c)/denominator
        else:
            return 0

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

line = Line.fromCoord(0, 1, 1, 0)
point = Point(0, 0)
print(line.distanceToPoint(point))
