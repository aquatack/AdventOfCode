# %% 1

def checker(grid: list[str], i: int, j: int) -> int:
    """Checks the given 2D array of characters at position i, j for the X-MAS pattern.
     e.g:  M  .  S
           .  A  .
           M  .  S """
    if i < 1 or i >= len(grid[0]) - 1:
        return 0
    if j < 1 or j >= len(grid) - 1:
        return 0

    if grid[i][j] != "A":
        return 0

    count = 0
    # now check the four points (top left, top right, btm left, btm right).
    # Each "MAS" can be reversed.
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


def search_grid(grid: list[str]) -> int:
    """Iterates through the provided 2D array for the X-MAS pattern.
    Returns an int representing the number of patterns found in the grid."""
    count = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            count += checker(grid, i, j)
    return count


ws_grid = []

with open('fulldata.txt', 'r', encoding='utf-8') as file:
    for line in file:
        row = line.strip()
        ws_grid.append(row)

print(search_grid(ws_grid))

