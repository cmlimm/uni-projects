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

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)


# check constructor
L = Line(2, 3, 4)
# check __str__()
print(L)

# check fromCoord
L = Line.fromCoord(-1, 0, 0, -1)
# check __str__()
print(L)

# check constructor
L = Line(3, -5, 6)
# check __str__()
print(L)

# check __str__()
L = Line.fromCoord(0, 1, 1, 0)
print(L)

# check __str__()
L = Line.fromCoord(2, 4, -3, 5)
# check __str__()
print(L)

# check constructor
L = Line(2, 3, -4)
# check __str__()
print(L)

# check constructor
L = Line(2, -3, -4)
# check __str__()
print(L)
