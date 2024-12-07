# %% 1

def get_map(file):
    map = []    
    with open(f'{file}', 'r', encoding='utf-8') as file:
        for line in file:
            elements = []
            for char in line.strip():
                elements.append(char)
            map.append(elements)
    return map


def print_map(map):
    for row in map:
        print("".join(row))

def find_guard(map):
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == "^":
                return i, j, "N"
            elif element == ">":
                return i, j, "E"
            elif element == "v":
                return i, j, "S"
            elif element == "<":
                return i, j, "W"
    return None



def check_for_obs(i, j, direction):
    try:    
        if direction == "N":
            if i-1 < 0:
                return False
            if map[i-1][j] == "#":
                return True
        elif direction == "E":
            if j+1 >= len(map[0]):
                return False
            if map[i][j+1] == "#":
                return True
        elif direction == "S":
            if i+1 >= len(map):
                return False
            if map[i+1][j] == "#":
                return True
        elif direction == "W":
            if j-1 < 0:
                return False
            if map[i][j-1] == "#":
                return True
    except IndexError:
        return False
    return False

def move(i, j, direction):
    map[i][j] = "X"
    
    if check_for_obs(i, j, direction):
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
            
        return i, j, direction
    
    if direction == "N":
        i -= 1
    elif direction == "E":
        j += 1
    elif direction == "S":
        i += 1
    elif direction == "W":
        j -= 1
    return i, j, direction
        

def move_guard(map, i, j, direction):
    iteration = 0
    while True:
        iteration += 1
        i, j, direction = move(i, j, direction)
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]):
            break
        #print("Iteration: ", iteration)
        #print_map(map)
    return i, j, direction        

def count_squares(map):
    count = 0
    for row in map:
        for element in row:
            if element == "X":
                count += 1
    return count


map = get_map("fulldata.txt")
i, j, direction = find_guard(map)
i, j, direction = move_guard(map, i, j, direction)
print("positions: ", count_squares(map))
# %%
