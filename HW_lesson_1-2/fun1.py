def f(x):
    if -2.4 <= x <= 5.7:
        return x**2
    else:
        return 4

x = float(input("Введите число: "))
print("f("+str(x)+") =", f(x))
