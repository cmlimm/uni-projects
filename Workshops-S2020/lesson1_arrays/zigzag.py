def zigzag(n):
    matrix = [n*[0] for _ in range(n)]
    number = 1

    for step in range(1, n+1):
        for num in range(step):
            if step % 2 == 0:
                matrix[num][step - 1 - num] = number
            if step % 2 == 1:
                matrix[step - 1 - num][num] = number
            number += 1

    number = n*n
    for step in range(1, n):
        for num in range(step):
            if step % 2 == 0:
                matrix[n - 1 - num][n - step + num] = number
            if step % 2 == 1:
                matrix[n - step + num][n - 1 - num] = number
            number -= 1

    return matrix

def pretty_print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

pretty_print_matrix(zigzag(5))
