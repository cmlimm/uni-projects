def maxim(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Наибольшее из введенных чисел:", maxim(a, b))
