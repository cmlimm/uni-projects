def BFS(graph, start):
    vert = range(len(graph))
    added = [False]*len(graph)
    queue = [start]
    added[start] = True
    result = [start]
    while queue != []:
        node = queue[0]
        del queue[0]
        children = []
        for n in vert:
            if graph[node][n] != 0:
                children.append(n)
        for child in children:
            if not added[child]:
                queue.append(child)
                added[child] = True
                result.append(child)
    return result

def component(graph):
    components = []
    not_seen = list(range(len(graph)))
    while not_seen != []:
        current = not_seen[0]
        seen = BFS(graph, current)
        components.append(seen)
        for node in seen:
            not_seen.remove(node)
    return components

def adjacency_matrix(garden_matrix):
    n = len(garden_matrix)
    m = len(garden_matrix[0])

    walls = [-1 for _ in range(n + 2)]
    for row in garden_matrix:
        row.insert(0, -1)
        row.append(-1)
    garden_matrix.insert(0, walls)
    garden_matrix.append(walls)

    single_counter = 0
    single = True
    adjacency = [(n*m+1)*[0] for _ in range(n*m+1)]

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if garden_matrix[x][y] != 0:
                number = (x-1)*m + y

                if garden_matrix[x+1][y] == 1:
                    number_neighbour = x*m + y
                    adjacency[number][number_neighbour] = 1
                    single = False

                if garden_matrix[x-1][y] == 1:
                    number_neighbour = (x-2)*m + y
                    adjacency[x*y][number_neighbour] = 1
                    single = False

                if garden_matrix[x][y+1] == 1:
                    number_neighbour = (x-1)*m + y + 1
                    adjacency[x*y][number_neighbour] = 1
                    single = False

                if garden_matrix[x][y-1] == 1:
                    number_neighbour = (x-1)*m + y - 1
                    adjacency[x*y][number_neighbour] = 1
                    single = False

                if single:
                    single_counter += 1
                single = True

    adjacency = adjacency[1:]
    adjacency = [row[1:] for row in adjacency]
    return adjacency, single_counter

def count_garden_components(garden_matrix):

    adj_singles = adjacency_matrix(garden_matrix)
    adjacency = adj_singles[0]
    single_counter = adj_singles[1]

    components = component(adjacency)
    components_counter = 0
    for comp in components:
        if len(comp) > 1:
            components_counter += 1

    return components_counter + single_counter

garden_matrix = [[1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]]
# garden_matrix = [[1, 1, 0],
#                  [0, 0, 1],
#                  [1, 0, 1]]
# garden_matrix = [[1, 1, 1],
#                  [1, 1, 1],
#                  [1, 1, 1]]

print(count_garden_components(garden_matrix))
