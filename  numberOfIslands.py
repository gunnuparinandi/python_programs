def number_islands(matrix):
    # type: (matrix) -> int
    if matrix is None or len(matrix) == 0:
        return 0

    num_islands = 0  # type: int

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 1:
                num_islands = num_islands + 1
                dfs(matrix, row, column)
    return num_islands


def dfs(matrix, row, column):
    if (column < 0 or column >= len(matrix[0])) or (row < 0 or row >= len(matrix)) or (matrix[row][column] == 0):
        return 0

    #sink island
    matrix[row][column] = 0
    dfs(matrix, row + 1, column)
    dfs(matrix, row - 1, column)
    dfs(matrix, row, column + 1)
    dfs(matrix, row, column - 1)

    return 1


# define matrix
w, h = 5, 6
g = [[0 for x in range(w)] for y in range(h)]


#print matrix g
g[0][0] = 1
g[1][2] = 1
g[1][3] = 1
g[2][1] = 1
g[2][2] = 1
g[4][0] = 1
g[4][1] = 1
g[5][0] = 1
g[5][1] = 1
g[4][4] = 1
g[5][4] = 1

print(g)

print(number_islands(g))