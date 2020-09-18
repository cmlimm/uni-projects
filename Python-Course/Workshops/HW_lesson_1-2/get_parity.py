def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False

a = int(input("Введите число: "))
if isEven(a):
    print("Число", a, "четное")
else:
    print("Число", a, "нечетное")
