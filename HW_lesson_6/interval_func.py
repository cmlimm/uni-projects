def fun(x):
    return x**2+3

sum = 0
for i in range(10, 30, 2):
    sum += fun(i)
print(sum)

