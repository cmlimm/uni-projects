def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    return [[matrix[column][row] for column in range(m)] for row in range(n)]

def sort_by_column(matrix):
    matrix = transpose(matrix)
    n = len(matrix)
    m = len(matrix[0])

    for step in range(n):
        min = 0
        for row in range(step+1, n):
            if matrix[row][0] < matrix[min][0]:
                min = row
        temp = matrix[0]
        matrix[0] = matrix[min]
        matrix[min] = temp

    matrix = transpose(matrix)
    return matrix

matrix = [[3,2,1],
          [6,5,4],
          [9,8,7]]
for row in sort_by_column(matrix):
    print(row)
