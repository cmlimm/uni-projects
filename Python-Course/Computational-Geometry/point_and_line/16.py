import math

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

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
        if a == 0:
            self.a = 0.0
        else:
            self.a = a
        if b == 0:
            self.b = 0.0
        else:
            self.b = b
        if c == 0:
            self.c = 0.0
        else:
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

    def perpendicularLine(self, point):
        a = -1
        b = (self.y1 - self.y2)
        c = (point.x - b*point.y)
        return Line(-a, -b, -c)

    def nearPoint(self, point):
        return self.intersection(self.perpendicularLine(point))

    def sidePoint(self, point):
        side = (point.x)*(self.y2 - self.y1) - (point.y - self.y1)
        if round(abs(math.fabs(side)), 4) < 0.001:
            return 'ON'
        elif side < 0:
            return 'LEFT'
        else:
            return 'RIGHT'

    def oneSide(self, point1, point2):
        side1 = self.sidePoint(point1)
        side2 = self.sidePoint(point2)
        match = [('LEFT', 'RIGHT'), ('RIGHT', 'LEFT')]
        if (side1, side2) not in match:
            return True
        else:
            return False

    def parallelLine(self, point):
        a = self.a
        b = self.b
        c = -(a*point.x + b*point.y)
        parallel = Line(-a, -b, -c)
        parallel.normalize()
        return parallel

    def projectionLength(self, point1, point2):
        near_point1 = self.nearPoint(point1)
        near_point2 = self.nearPoint(point2)
        return near_point1.distanceTo(near_point2)

    def middlePoint(self, point):
        near_point = self.nearPoint(point)
        x = (point.x + near_point.x)/2
        y = (point.y + near_point.y)/2
        return Point(x, y)

    def symmetricPoint(self, point):
        near_point = self.nearPoint(point)
        x = 2*near_point.x - point.x
        y = 2*near_point.y - point.y
        return Point(x, y)

    def insideTreug(self, point):
        if self.c == 0 or self.a == 0 or self.b == 0:
            return False

        axis_x = -self.c / self.a
        axis_y = -self.c / self.b

        if axis_x < 0 and (point.x < axis_x or point.x > 0):
            return False
        if axis_x > 0 and (point.x > axis_x or point.x < 0):
            return False

        if axis_y < 0 and (point.y < axis_y or point.y > 0):
            return False
        if axis_y > 0 and (point.y > axis_y or point.y < 0):
            return False

        line_x = - (self.c + self.b*point.y)/self.a
        line_y = - (self.c + self.a*point.x)/self.b

        if axis_y < 0 and point.y < line_y:
            return False
        if axis_y > 0 and point.y > line_y:
            return False

        if axis_x < 0 and point.x < line_x:
            return False
        if axis_x > 0 and point.x > line_x:
            return False

        return True

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(float(y1-y2), float(x2-x1), float(x1*y2-x2*y1))

line1 = Line.fromCoord(0, 1, 1, 0)
point1 = Point(3, 3)
print(line1.insideTreug(point1))

line2 = Line.fromCoord(0, 1, 1, 0)
point2 = Point(0.25, 0.1)
print(line2.insideTreug(point2))

line3 = Line.fromCoord(13.18, 14.29, -6.91, -3.40)
point3 = Point(8.72, 2.81)
print(line3.insideTreug(point3))

line4 = Line.fromCoord(-5.43, 7.71, 12.76, 6.81)
point4 = Point(13.86, 2.25)
print(line4.insideTreug(point4))

line5 = Line.fromCoord(-12.91, -8.19, 8.59, -6.41)
point5 = Point(7.62, 1.11)
print(line5.insideTreug(point5))

line6 = Line.fromCoord(-7.53, -14.06, 7.54, 5.00)
point6 = Point(7.42, -3.01)
print(line6.insideTreug(point6))
