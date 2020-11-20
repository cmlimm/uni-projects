import math


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f})'.format(self.x, self.y, self.z)

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def norm(self):
        l = self.len()
        if l:
            return Vector3(self.x / l, self.y / l, self.z / l)
        else:
            return Vector3(0, 0, 0)

    def xR(self, a):
        return Vector3(self.x * a, self.y * a, self.z * a)

    def plusV(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def minusV(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotV(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def xV(self, v):
        return Vector3(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )


class Matrix3x3:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def __str__(self):
        return '(({:.2f}, {:.2f}, {:.2f}),\n ({:.2f}, {:.2f}, {:.2f}),\n ({:.2f}, {:.2f}, {:.2f}))'.format(
            self.v1.x, self.v1.y, self.v1.z,
            self.v2.x, self.v2.y, self.v2.z,
            self.v3.x, self.v3.y, self.v3.z,
        )

    @staticmethod
    def I():
        return Matrix3x3(Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1))

    def xR(self, a):
        return Matrix3x3(self.v1.xR(a), self.v2.xR(a), self.v3.xR(a))

    def plusM(self, m):
        return Matrix3x3(self.v1.plusV(m.v1), self.v2.plusV(m.v2), self.v3.plusV(m.v3))

    def minusM(self, m):
        return Matrix3x3(self.v1.minusV(m.v1), self.v2.minusV(m.v2), self.v3.minusV(m.v3))

    def xV(self, v):
        return Vector3(self.v1.dotV(v), self.v2.dotV(v), self.v3.dotV(v))

    def xM(self, m):
        v1 = Vector3(m.v1.x, m.v2.x, m.v3.x)
        v2 = Vector3(m.v1.y, m.v2.y, m.v3.y)
        v3 = Vector3(m.v1.z, m.v2.z, m.v3.z)
        return Matrix3x3(
            Vector3(self.v1.dotV(v1), self.v1.dotV(v2), self.v1.dotV(v3)),
            Vector3(self.v2.dotV(v1), self.v2.dotV(v2), self.v2.dotV(v3)),
            Vector3(self.v3.dotV(v1), self.v3.dotV(v2), self.v3.dotV(v3)),
        )

    @staticmethod
    def MRot(v, r):
        s = Matrix3x3(Vector3(0, v.z, -v.y), Vector3(-v.z, 0, v.x), Vector3(v.y, -v.x, 0))
        slag1 = Matrix3x3.I()
        slag2 = s.xR(math.sin(r))
        slag3 = s.xM(s).xR(1-math.cos(r))
        return slag1.plusM(slag2).plusM(slag3)
