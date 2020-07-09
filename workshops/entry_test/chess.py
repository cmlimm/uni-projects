def same_color(x1, y1, x2, y2):
    same_row = (x2 - x1) % 2 + 1
    same_column = (y2 - y1) % 2 + 1

    return same_row == same_column

def queen(x1, y1, x2, y2):
    if y1 == y2:
        return True
    if x1 == x2:
        return True

    if abs(x2 - x1) == abs(y2 - y1):
        return True

    return False

def knight(x1, y1, x2, y2):
    moves = [[-2, -1], [-2, +1], [+2, -1], [+2, +1], [-1, -2], [-1, +2], [+1, -2], [+1, +2]]
    for move in moves:
        if x1 + move[0] == x2 and y1 + move[1] == y2:
            return True

    return False

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print("Клетки одного цвета: ", same_color(x1, y1, x2, y2))
print("Ферзь на первой клетке бьет вторую клетку: ", queen(x1, y1, x2, y2))
print("Конь на первой клетке бьет вторую клетку: ", knight(x1, y1, x2, y2))
