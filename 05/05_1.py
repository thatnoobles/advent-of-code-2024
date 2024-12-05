import math

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
    if valid_order(rules, update):
        print(update)
        total += update[math.floor(len(update) / 2)]

print(total)