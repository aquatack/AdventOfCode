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


def checker(grid, i, j):
    if i < 1 or i >= len(grid[0]) - 1:
        return 0
    if j < 1 or j >= len(grid) - 1:
        return 0

    if grid[i][j] != "A":
        return 0

    count = 0
    # now check the four points (top left, top right, btm left, btm right)
    valid_cases = [["M", "S", "M", "S"], ["S", "S", "M", "M"],
                   ["M", "M", "S", "S"], ["S", "M", "S", "M"]]

    for case in valid_cases:
        if grid[i-1][j-1] != case[0]:
            continue
        if grid[i+1][j-1] != case[1]:
            continue
        if grid[i-1][j+1] != case[2]:
            continue
        if grid[i+1][j+1] != case[3]:
            continue
        count += 1

    return count


def search_grid(grid):
    count = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            count += checker(grid, i, j)
    return count


print(search_grid(ws_grid))
