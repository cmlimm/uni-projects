from math import sqrt

def is_small(a, b, c, r):
    p = (a + b + c)/2
    return r <= sqrt((p-a)*(p-b)*(p-c)/p)

a = int(input())
b = int(input())
c = int(input())
r = int(input())
print(is_small(a, b, c, r))
