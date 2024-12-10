FREE_SPACE = -1

def next_free_position(filesystem: list[int]):
    for i in range(len(filesystem)):
        if filesystem[i] == FREE_SPACE:
            return i
    return -1

def occupied_positions(filesystem: list[int]):
    total = 0

    for i in range(len(filesystem)):
        if filesystem[i] != FREE_SPACE:
            total += 1
    return total

def get_checksum(filesystem: list[int]):
    total = 0

    for i in range(len(filesystem)):
        if filesystem[i] != FREE_SPACE:
            total += filesystem[i] * i

    return total

###########################

filesystem = []

with open("input.txt", "r") as file:
    current_id = 0
    content = file.read()

    for i in range(len(content.strip())):
        if i % 2 == 0:  # even pos = file present
            filesystem += [current_id] * int(content[i])
            current_id += 1
        else:           # odd pos = empty space
            filesystem += [FREE_SPACE] * int(content[i])

current_pos = len(filesystem) - 1
while current_pos >= next_free_position(filesystem):
    filesystem[next_free_position(filesystem)] = filesystem[current_pos]
    filesystem[current_pos] = FREE_SPACE
    current_pos -= 1

print(get_checksum(filesystem))