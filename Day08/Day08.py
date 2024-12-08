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

def print_map(map):
    for row in map:
        print("".join(row))
        
room_map, antenna_positions = get_map("Day08/fulldata.txt")
xmax = len(room_map[0])
ymax = len(room_map)
print_map(room_map)
print(antenna_positions)


#    a   b   c   :   2(b-a) = (c-a)
# 2b-2a = c-a
#2b-c = 3a
#a = (2b-c)/3
def find_antenna_antinodes(positions, xmax, ymax):
    antinodes = set()
    for i, ant1 in enumerate(positions):
        for j, ant2 in enumerate(positions):
            if i != j:
                y = ant1[0] - (ant2[0] - ant1[0])
                x = ant1[1] - (ant2[1] - ant1[1])
                if x < 0 or x >= xmax or y < 0 or y >= ymax:
                    continue
                antinodes.add((y, x))
                
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
print(f"unique_antinodes {len(unique_antinodes)}: ", unique_antinodes)