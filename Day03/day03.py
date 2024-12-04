import re

# memorystring : str = ""
memory = []
with open('Day03/fulldata.txt', 'r') as file:
    # Read each line from the file

    for line in file:
        memory.append(line.strip())


def getproduct(match: str) -> int:
    print(match)
    # string off the "mul(" and ")" parts
    digit_string = match[4:-1]  # e.g. "123,456"
    num1, num2 = map(int, digit_string.split(','))  # split on the comma
    product = num1 * num2
    print(num1, num2, "product:", product)
    return product


cumsum = 0
items = []
do_state = True
for line in memory:
    print(line)
    matches = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))?(don't)?(do)?", line)
    # print(matches)
    for match in matches:
        for item in match:
            if item == "":
                continue
            items.append(item)

print(items)
for item in items:
    print(item)
    if "don't" in item:
        do_state = False
        continue
    if "do" in item:
        do_state = True
        continue

    if do_state:
        cumsum += getproduct(item)


print(cumsum)
