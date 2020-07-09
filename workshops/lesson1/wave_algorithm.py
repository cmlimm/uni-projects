def get_path(matrix, begin, end):
    current = end
    path = [(end[0]-1, end[1]-1)]
    while current != begin:
        x = current[0]
        y = current[1]
        current_counter = matrix[x][y]

        if matrix[x+1][y] == current_counter - 1:
            current = (x+1, y)
        elif matrix[x-1][y] == current_counter - 1:
            current = (x-1, y)
        elif matrix[x][y+1] == current_counter - 1:
            current = (x, y+1)
        elif matrix[x][y-1] == current_counter - 1:
            current = (x, y-1)

        path.append((current[0]-1, current[1]-1))

    return path

def wave(matrix, begin, end):
    n = len(matrix)
    matrix[begin[0]][begin[1]] = -2

    walls = [-1 for _ in range(n + 2)]

    for row in matrix:
        row.insert(0, -1)
        row.append(-1)

    matrix.insert(0, walls)
    matrix.append(walls)

    end = (end[0]+1, end[1]+1)
    begin = (begin[0]+1, begin[1]+1)

    current = [begin]
    future = []
    counter = 1

    while end not in current:
        for node in current:
            x = node[0]
            y = node[1]
            if matrix[x+1][y] == 0:
                matrix[x+1][y] = counter
                future.append((x+1, y))
            if matrix[x-1][y] == 0:
                matrix[x-1][y] = counter
                future.append((x-1, y))
            if matrix[x][y+1] == 0:
                matrix[x][y+1] = counter
                future.append((x, y+1))
            if matrix[x][y-1] == 0:
                matrix[x][y-1] = counter
                future.append((x, y-1))
        current = future
        future = []
        counter += 1

    matrix[begin[0]][begin[1]] = 0

    path = get_path(matrix, begin, end)

    matrix = matrix[1:-1]
    matrix = [row[1:-1] for row in matrix]
    return matrix, path

def pretty_print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

matrix = [[-1,  0, 0, 0, 0],
          [ 0,  0, 0, 0, 0],
          [ 0, -1, 0, 0, 0],
          [ 0, -1, 0, 0, 0],
          [ 0,  0, 0, 0, 0]]
begin = (1, 0)
end = (4, 4)

result = wave(matrix, begin, end)
pretty_print_matrix(result[0])
print(result[1])
