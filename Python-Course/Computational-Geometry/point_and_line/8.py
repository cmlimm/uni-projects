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
        self.x1 = 0
        self.x2 = 1
        if b != 0:
            self.y1 = -self.c/self.b
            self.y2 = (-self.c - self.a)/self.b
        else:
            self.y1 = -self.c
            self.y2 = -self.c - self.a

    def __str__(self):
        if self.a >= 0:
            str_a = '{:.2f}'.format(self.a)
        else:
            str_a = '-{:.2f}'.format(math.fabs(self.a))

        if self.b >= 0:
            str_b = '+ {:.2f}'.format(self.b)
        else:
            str_b = '- {:.2f}'.format(math.fabs(self.b))

        if self.c >= 0:
            str_c = '+ {:.2f}'.format(self.c)
        else:
            str_c = '- {:.2f}'.format(math.fabs(self.c))

        return '{}x {}y {} = 0'.format(str_a, str_b, str_c)

    def distanceToZero(self):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return math.fabs(self.c)/denominator
        else:
            return 0

    def distanceToPoint(self, point):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return math.fabs(self.a*point.x + self.b*point.y + self.c)/denominator
        else:
            return 0

    def isParallel(self, line):
        if abs(self.a*line.b - self.b*line.a) <= 0.001:
            return True
        else:
            return False

    def intersection(self, line):
        if not self.isParallel(line):
            det_x = self.b*line.c - self.c*line.b
            det_y = self.c*line.a - self.a*line.c
            det = self.a*line.b - self.b*line.a
            intersection_point = Point(det_x/det, det_y/det)
            return intersection_point
        else:
            return 'NO'

    def normalize(self):
        if self.c != 0:
            self.a = self.a / self.c
            self.b = self.b / self.c
            self.c = 1.0
        elif self.a != 0:
            self.b = self.b / self.a
            self.a = 1.0
            self.c = 0.0
        else:
            self.b = 1.0
            self.a = 0.0
            self.c = 0.0

    def perpendicular(self, point):
        a = -1
        b = (self.y1 - self.y2)
        c = (point.x - b*point.y)
        return Line(a, b, c)

    def nearPoint(self, point):
        return self.intersection(self.perpendicular(point))

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(float(y1-y2), float(x2-x1), float(x1*y2-x2*y1))

line1 = Line.fromCoord(0, 1, 1, 0)
point1 = Point(3, 4)
print(line1.nearPoint(point1))

line2 = Line.fromCoord(1, 0, 0, 1)
point2 = Point(3, 3)
print(line2.nearPoint(point2))
