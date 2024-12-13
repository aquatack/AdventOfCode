def get_map(file):
    room_map = []    
    antenna_positions = {}
    with open(f'{file}', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            elements = []
            for j, char in enumerate(line.strip()):
                elements.append(char)
                if char != ".":
                    antenna_positions.setdefault(char, set()).add((i, j))
            room_map.append(elements)
    return room_map, antenna_positions

def print_map(map, antinodes = None):
    if antinodes:
        for i, row in enumerate(map):
            for j, col in enumerate(row):
                if (i, j) in antinodes:
                    print("X", end="")
                else:
                    print(col, end="")
            print()
    else:
        for row in map:
            print("".join(row))
        


def equation_of_a_straight_line(pos1, pos2):
    m: float = (pos2[0] - pos1[0]) / (pos2[1] - pos1[1])
    c: float = pos1[0] - m * pos1[1]
    return m, c

def get_line_integers(pos1, pos2):
    y_delta = (pos2[0] - pos1[0]) 
    x_delta = (pos2[1] - pos1[1])
    return x_delta, y_delta

def find_antenna_antinodes(positions, xmax, ymax):
    antinodes = set()
    for i, ant1 in enumerate(positions):
        for j, ant2 in enumerate(positions):
            if i != j:
                #m, c = equation_of_a_straight_line(ant1, ant2)
                x_delta, y_delta = get_line_integers(ant1, ant2)
                for k in range(-1*max(xmax, ymax), max(xmax,ymax)):
                    
                    x = ant1[1] + k*x_delta
                    y = ant1[0] + k*y_delta
                    
                    if x < 0 or x >= xmax or y < 0 or y >= ymax:
                        continue

                    antinodes.add((int(y), int(x)))

                
    return antinodes

def find_all_antinodes(antenna_positions, xmax, ymax):
    antinodes = {}
    for ant_name, positions in antenna_positions.items():
        antinodes[ant_name] = find_antenna_antinodes(positions, xmax, ymax)

    return antinodes



def find_unique_antinodes(antinodes):
    unique_antinodes = set()
    for ant in antinodes.keys():
        for point in antinodes[ant]:
            unique_antinodes.add(point)
    return unique_antinodes

room_map, antenna_positions = get_map("Day08/fulldata.txt")
xmax = len(room_map[0])
ymax = len(room_map)
print_map(room_map)
#print("antenna positions: ", antenna_positions)

antinodes = find_all_antinodes(antenna_positions, xmax, ymax)
#print("antindoes: ",antinodes)

unique_antinodes = find_unique_antinodes(antinodes)
print_map(room_map, unique_antinodes)
print(f"unique_antinodes {len(unique_antinodes)}")