def is_animorph(number):
    string_number = str(number)
    length_number = len(string_number)
    square = number*number
    string_square = str(square)

    return string_square[-length_number::] == string_number

number = int(input())
print(is_animorph(number))
