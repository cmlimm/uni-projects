def is_latin_square(matrix, n):

    if len(matrix) != n:
        return False
    if len(matrix[0]) != n:
        return False

    full_set = set(range(1, n + 1))
    for i in range(n):
        ith_row = set(matrix[i])
        ith_column = set(matrix[j][i] for j in range(n))
        if ith_row != full_set or ith_column != full_set:
            return False
    return True

matrix = [[1, 2, 3],
          [2, 3, 1],
          [3, 1, 2]]
n = 3
print(is_latin_square(matrix, n))
