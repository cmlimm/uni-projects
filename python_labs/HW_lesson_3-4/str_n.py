def str_n(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s.lower()

s = input('Введите строку: ')
n = int(input('Введите число: '))
print(str_n(s, n))
