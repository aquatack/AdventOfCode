ws_grid = []

with open('Day04/fulldata.txt', 'r') as file:
    for line in file:
        row = (line.strip())
        ws_grid.append(row)

# row, column indexing
row_length = len(ws_grid[0])
col_length = len(ws_grid)

print("row length: ", row_length, "col length: ", col_length)
print(ws_grid[0][3])


def checker(grid, i, j, inci, incj):
    if i + 3 * inci >= len(grid[0]) or i + 3 * inci < 0:
        return 0
    if j + 3 * incj >= len(grid) or j + 3 * incj < 0:
        return 0

    if grid[i][j] == "X":
        if grid[i + inci][j + incj] == "M":
            if grid[i + 2 * inci][j + 2 * incj] == "A":
                if grid[i + 3 * inci][j + 3 * incj] == "S":
                    return 1

    return 0


def search_xmas_str(grid, i, j):
    count = 0
    count += checker(grid, i, j, 0, 1)
    count += checker(grid, i, j, 1, 1)
    count += checker(grid, i, j, 1, 0)
    count += checker(grid, i, j, 1, -1)
    count += checker(grid, i, j, 0, -1)
    count += checker(grid, i, j, -1, -1)
    count += checker(grid, i, j, -1, 0)
    count += checker(grid, i, j, -1, 1)

    return count


def search_grid(grid):
    count = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            count += search_xmas_str(grid, i, j)
    return count

# print(search_xmas_str(ws_grid,0,4))


print(search_grid(ws_grid))
