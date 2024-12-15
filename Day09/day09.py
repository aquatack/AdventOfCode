def get_map(file):
    maps = []
    with open(f'{file}', 'r', encoding='utf-8') as file:

        for i, line in enumerate(file):
            map_pairs = []   
            for j, char in enumerate(line.strip()):
                if j % 2 ==0:
                    pair = {}
                    map_pairs.append(pair)
                    pair["id"] = int(j/2)
                    pair["f_len"] = int(char)
                else:
                    map_pairs[-1]["s_len"] = int(char)

                #if char != ".":
                 #   antenna_positions.setdefault(char, set()).add((i, j))
            maps.append(map_pairs)
    return maps

def generate_disk(disk_map):
    map_array = []
    for pair in disk_map:
        if pair["f_len"] is not None:
            for i in range(pair["f_len"]):
                map_array.append(str(pair["id"]))
        try:
            for i in range(pair["s_len"]):
                map_array.append(".")
        except:
            continue
    #print(map_string)
    return map_array

def find_next_free(disk):
    for i, char in enumerate(disk):
        if char == ".":
            return i        
    return -1

def is_disk_compressed(disk):
    file_found = False
    for i, char in enumerate(reversed(disk)):
        if char == ".":
            if file_found:
                return False
        else:
            file_found = True
            
    return True  

def find_last_file_block(disk):
    for i,  char in enumerate(reversed(disk)):
        if char != ".":
            return len(disk) - i - 1
        
    return -1
        

def compress(disk):
    p_next_free = find_next_free(disk)
    p_file_block = find_last_file_block(disk)
    compressed_disk = disk.copy()
    while not is_disk_compressed(compressed_disk) and p_next_free != -1 and p_file_block != -1:
        temp = compressed_disk[p_next_free]
        compressed_disk[p_next_free] = compressed_disk[p_file_block]
        compressed_disk[p_file_block] = temp
        p_next_free = find_next_free(compressed_disk)
        p_file_block = find_last_file_block(compressed_disk)
        print_disk(compressed_disk)
        #print(compression_map.pop())
        
    return compressed_disk
        
def print_disk(disk):
    map_string = ""
    for item in disk:
        map_string += item
    print(map_string)
    
def calc_checksum(disk_map):
    checksum = 0
    for i,id in enumerate(disk_map):
        if id != ".":
            checksum += i*int(id)
    return checksum


disk_map = get_map("Day09/testdata.txt")[0]
disk = generate_disk(disk_map)
print_disk(disk)
compressed_disk = compress(disk)

checksum = calc_checksum(compressed_disk)
print("checksum: ", checksum)
