import itertools

def load_file(file):
    with open(f'{file}', 'r', encoding='utf-8') as file:
        testdata = []
        for i, line in enumerate(file):
            result: int
            elements = []
            result, rhs = line.strip().split(":")
            elements = map((int),rhs.strip().split(" "))
            testdata.append({"result": int(result),"elements": list(elements)})
    return testdata


    
def generate_operator_combinations(elements):
    n_ops = len(elements)-1
    # there will be 2^ combinations
    operators = ["+","*","||"]
    operations = list(itertools.product(operators, repeat = n_ops))
    #print(operations)
    
    return operations
    
#def built_list(item):

def apply_functions(elements, operators):
    cum_result = elements[0]
    for i, element in enumerate(elements[1:]):
        #print(i)        
        #print(elements)
        #print(element)

        if operators[i] == "+":
            cum_result += element
        if operators[i] == "*":
            cum_result *= element
        if operators[i] == "||":
            cum_result = int(str(cum_result) + str(element))
    
    return cum_result

testdata = load_file("Day07/fulldata.txt")

success_count = 0
success_value = 0
for item in testdata:  
    item["success"] = False
    print("result: ", item["result"], ". items: ", item["elements"])
    
    operations = generate_operator_combinations(item["elements"])
    # work through each of the possible operator combinations
    
    for operator in operations:
        result = apply_functions(item["elements"], operator)
        if result == int(item["result"]):
            item["success"] = True
            break
            
    #print(result)
    #
    if item["success"] == True:
        success_count += 1
        success_value += item["result"]
    
    
print("successes: ", success_count, "success value: ", success_value)