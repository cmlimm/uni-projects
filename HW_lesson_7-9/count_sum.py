number = input("Введите число: ")
oddDigits = [int(i)**2 for i in number if int(i) % 2 != 0]
print(sum(oddDigits))
