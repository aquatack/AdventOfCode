import re

#memorystring : str = ""
memory = []
with open('Day03/testdata.txt', 'r') as file:
    # Read each line from the file
    
    for line in file:
        memory.append(line.strip())

def getproduct(match: str) -> int:
    print(match)
    # string off the "mul(" and ")" parts
    digit_string = match[4:-1] # e.g. "123,456"
    num1, num2 = map(int, digit_string.split(',')) # split on the comma
    product = num1 * num2
    print(num1, num2, "product:", product)
    return product

for line in memory:
    print(line)
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    print(matches)
    cumsum = 0
    for match in matches:
        cumsum += getproduct(match)
        print(cumsum)
