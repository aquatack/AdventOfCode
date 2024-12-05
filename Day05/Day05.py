rules_str = []
updates = []

with open('Day05/fulldata.txt', 'r', encoding='utf-8') as file:
    rulesmode = True
    for line in file:
        if line.strip() == "":
            rulesmode = False
            continue

        if rulesmode:
            rules_str.append(line.strip())
        else:
            pages = list(map(int,line.strip().split(",")))
            updates.append(pages)

# print("rules: ", rules_str)
# print("updates: ", updates)

# build dictionary from the rules
def parse_rules(rules: list[str]) -> dict[int, list[int]]:
    rules_dict = {}
    for rule in rules:
        k, v = map(int, rule.split("|"))
        if k not in rules_dict:
            rules_dict[k] = []
        rules_dict[k].append(v)
    return rules_dict

rules = parse_rules(rules_str)
#print(rules)

def is_valid(page, prior_pages, rules) -> bool:
    # check that prior_pages does not contain a value referenced by
    # rules for page

    rule = rules.get(page)
    if rule is None:
        return True, 0

    for i, prior_page in enumerate(prior_pages):
        for r in rule:
            if prior_page == r:
                return False, i
        
    return True, 0

# # 75,47,61,53,29
# print(is_valid(75,[], rules)) # true
# print(is_valid(47,[75],rules)) # true
# print(is_valid(61,[75,47],rules)) # true
# print(is_valid(53,[75,47,61],rules)) # true
# print(is_valid(29,[75,47,61,53],rules)) # true

# # 75,97,47,61,53
# print(is_valid(97,[75],rules)) # false

def is_valid_update(update, rules):
    for i, element in enumerate(update):
        #print(element)
        #print(update[:i])
        valid, conflict_i = is_valid(element, update[:i], rules)
        if not valid:
            return False, i, conflict_i, 
    return True, 0, 0

cumval = 0
incorrect_updates = []
for update in updates:
    valid, i, conflict_i = is_valid_update(update, rules)
    if valid:
        #print("valid: ", update, "index: ", int((len(update) - 1) / 2))
        cumval += update[int((len(update) - 1) / 2)]
    else:
        incorrect_updates.append(update)

print("correctly ordered pages: ", cumval)

cumval = 0
for update in incorrect_updates:
    valid = False
    while not valid:
        valid, i, conflict_i = is_valid_update(update, rules)
        update[i], update[conflict_i] = update[conflict_i], update[i]
        valid, i, conflict_i = is_valid_update(update, rules)
        #print(element)
        #print(update[:i])
        #if not is_valid(element, update[:i], rules):
        print(update, valid)
    cumval += update[int((len(update) - 1) / 2)]
        
    
print("newly valids: ", cumval)