# %% 1
import copy
import concurrent.futures

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
                map[i][j] = "X"
                return i, j, "N"
            elif element == ">":
                map[i][j] = "X"
                return i, j, "E"
            elif element == "v":
                map[i][j] = "X"
                return i, j, "S"
            elif element == "<":
                map[i][j] = "X"
                return i, j, "W"
    return None



def check_for_obs(i, j, direction, map):
    try:    
        if direction == "N":
            if i < 0:
                return False
            if map[i][j] == "#":
                return True
        elif direction == "E":
            if j >= len(map[0]):
                return False
            if map[i][j] == "#":
                return True
        elif direction == "S":
            if i >= len(map):
                return False
            if map[i][j] == "#":
                return True
        elif direction == "W":
            if j < 0:
                return False
            if map[i][j] == "#":
                return True
    except IndexError:
        return False
    return False

def move(i, j, direction, map):
    
    if direction == "N":
        if not check_for_obs(i-1, j, direction, map):
            i -= 1
        else:
            direction = "E"
    elif direction == "E":
        if not check_for_obs(i, j+1, direction, map):
            j += 1
        else:
            direction = "S"
    elif direction == "S":
        if not check_for_obs(i+1, j, direction, map):
            i += 1
        else:
            direction = "W"
    elif direction == "W":
        if not check_for_obs(i, j-1, direction, map):
            j -= 1
        else:
            direction = "N"
    
    if i >= 0 and j >= 0 and i < len(map) and j < len(map[0]):
        map[i][j] = "X"
        
    return i, j, direction, map
        

def move_guard(map, i, j, direction, position_record = []):
    iteration = 0
    looping = False
    previously_stable = False
    previous_map = copy.deepcopy(map)
    stable = False
    #position_record.append((i, j, direction))
    while True:
        iteration += 1
        i, j, direction, map = move(i, j, direction, map)
        position_record.append((i, j, direction))
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]):
            break
        #print("Iteration: ", iteration)
        #print_map(map)
        if iteration % 1000 == 0:
            #print("Iteration: ", iteration)
            
            if compare_maps(map, previous_map):
                #print("Stable")
                #previously_stable = stable
                
                #stable = True
                #if previously_stable == True and stable == True:
                looping = True
                return i, j, direction, looping
            previous_map = copy.deepcopy(map)
            
        
    return i, j, direction, looping   

def count_squares(map):
    count = 0
    for row in map:
        for element in row:
            if element == "X":
                count += 1
    return count

def compare_maps(map1, map2):
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return False
    return True



original_map = get_map("Day06/fulldata.txt")
map = copy.deepcopy(original_map)
guard_pos = find_guard(map)
if guard_pos is not None:
    i, j, direction = guard_pos
print("Initial position: ", i, j, direction)
position_record = []
i, j, direction, looping = move_guard(map, i, j, direction, position_record)
print("positions: ", count_squares(map))

print("path points: ", len(position_record))


def try_a_blocker_to_cause_looping(map, i_block, j_block):
    map[i_block][j_block] = "#"
    if guard_pos is not None:
        i, j, direction = guard_pos
    else:
        return False
    i, j, direction, looping = move_guard(map, i, j, direction, list())
    if looping:
        return True    
    return False

def find_blocker(original_map, position_record):
    loops_found = 0
    
    def process_blocker(position):
        i_block, j_block = position
        print(f"Trying blocker at: {i_block}, {j_block}")
        map_copy = copy.deepcopy(original_map)
        if try_a_blocker_to_cause_looping(map_copy, i_block, j_block):
            print(f"Loop found caused by blocker at: {i_block}, {j_block}")
            return 1
        return 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_blocker, position_record))

    loops_found = sum(results)
    return loops_found
    
    # for iteration, position in enumerate(position_record):
    #     i_block, j_block = position
    #     print(f"Trying blocker {iteration}/{len(position_record)} at: ", i_block, j_block)
    #     map = copy.deepcopy(original_map)
    #     if try_a_blocker_to_cause_looping(map, i_block, j_block):
    #         print("Loop found caused by blocker at: ", i_block, j_block)
    #         loops_found += 1
    #     #print_map(map)
    # return loops_found

def generate_search_map(position_record, map):
    search_map = set()
    for pos in position_record:
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(map) and pos[1] < len(map[0]):
            search_map.add((pos[0], pos[1]))

    i, j, direction = find_guard(map)
    search_map.discard((i, j))
    return search_map

print_map(original_map)
map = copy.deepcopy(original_map)
search_map = generate_search_map(position_record, map)
print("search map: ", search_map)
print("path points: ", len(search_map))

print("loops found: ", find_blocker(map, list(search_map)))
# %%
