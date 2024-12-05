import math

# check entire update
def valid_order(rules: dict[int, list[int]], update: list[int]) -> bool:
    key = update[0]

    for i in range(1, len(update)):
        if key not in rules:
            if key in rules[update[i]]:
                return False
        elif update[i] not in rules[key]:
            return False
        else:
            key = update[i]
    return True

######################

rules = {}
updates = []
total = 0

with open("input.txt", "r") as file:
    file_split = file.read().split("\n\n")

    for rule in file_split[0].split("\n"):
        key = int(rule.split("|")[0])
        val = int(rule.split("|")[1])
        
        if key not in rules:
            rules[key] = []
        rules[key].append(val)
    
    updates_raw = file_split[1].split("\n")

    for update in updates_raw:
        updates_split = update.split(",")
        updates.append([int(num) for num in updates_split])

for update in updates:
    if not valid_order(rules, update):
        corrected_order = [update[0]]

        for i in range(1, len(update)):
            page = update[i]

            index_to_insert = 0
            valid_order_found = False

            while index_to_insert < len(corrected_order) and not valid_order_found:
                corrected_order.insert(index_to_insert, page)
                
                if valid_order(rules, corrected_order):
                    valid_order_found = True
                else:
                    corrected_order.pop(index_to_insert)
                    index_to_insert += 1

            if not valid_order_found:
                corrected_order.append(page)

        total += corrected_order[math.floor(len(corrected_order) / 2)]

print(total)