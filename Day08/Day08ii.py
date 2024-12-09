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
        
room_map, antenna_positions = get_map("Day08/fulldata.txt")
xmax = len(room_map[0])
ymax = len(room_map)
print_map(room_map)
print(antenna_positions)

def equation_of_a_straight_line(pos1, pos2):
    m: float = (pos2[0] - pos1[0]) / (pos2[1] - pos1[1])
    c: float = pos1[0] - m * pos1[1]
    return m, c

def find_antenna_antinodes(positions, xmax, ymax):
    antinodes = set()
    for i, ant1 in enumerate(positions):
        for j, ant2 in enumerate(positions):
            if i != j:
                m, c = equation_of_a_straight_line(ant1, ant2)
                for x in range(0, xmax):
                    y: float = m * x + c
                    
                    if x < 0 or x >= xmax or y < 0 or y >= ymax:
                        continue
                    if y % 1 < 0.01: # to avoid float comparison error
                        print(f"y: {y}, x: {x}")
                        antinodes.add((int(y), int(x)))
                    else:
                        print(f"y: {y}, x: {x}, y%1: {y%1}")
                
    return antinodes

def find_all_antinodes(antenna_positions, xmax, ymax):
    antinodes = {}
    for ant_name, positions in antenna_positions.items():
        antinodes[ant_name] = find_antenna_antinodes(positions, xmax, ymax)

    return antinodes

antinodes = find_all_antinodes(antenna_positions, xmax, ymax)
print("antindoes: ",antinodes)

def find_unique_antinodes(antinodes):
    unique_antinodes = set()
    for ant in antinodes.keys():
        for point in antinodes[ant]:
            unique_antinodes.add(point)
    return unique_antinodes

unique_antinodes = find_unique_antinodes(antinodes)
print_map(room_map, unique_antinodes)
print(f"unique_antinodes {len(unique_antinodes)}")