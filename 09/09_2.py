import sys
FREE_SPACE = -1

# returns (position, size) of next available free space
def free_positions_and_sizes(filesystem: list[int]):
    result = []

    i = 0
    while i < len(filesystem):
        if filesystem[i] == FREE_SPACE:
            size = 1
            while i + size < len(filesystem) and filesystem[i + size] == FREE_SPACE:
                size += 1
            result.append((i, size))
            i += size
        else:
            i += 1
    return result

def get_checksum(filesystem: list[int]):
    total = 0

    for i in range(len(filesystem)):
        if filesystem[i] != FREE_SPACE:
            total += filesystem[i] * i

    return total

###########################

filesystem = []
file_positions_sizes = {}

with open("input.txt", "r") as file:
    current_id = 0
    content = file.read()

    for i in range(len(content.strip())):
        if i % 2 == 0:  # even pos = file present
            file_positions_sizes[current_id] = (len(filesystem), int(content[i]))
            filesystem += [current_id] * int(content[i])
            current_id += 1
        else:           # odd pos = empty space
            filesystem += [FREE_SPACE] * int(content[i])

for file_id in sorted(file_positions_sizes.keys(), reverse=True):

    available_spaces = free_positions_and_sizes(filesystem)
    
    for space in available_spaces:
        if space[1] >= file_positions_sizes[file_id][1] and space[0] < file_positions_sizes[file_id][0]:
            filesystem[space[0] : space[0] + file_positions_sizes[file_id][1]] = [file_id] * file_positions_sizes[file_id][1]
            filesystem[file_positions_sizes[file_id][0] : file_positions_sizes[file_id][0] + file_positions_sizes[file_id][1]] = [FREE_SPACE] * file_positions_sizes[file_id][1]
            file_positions_sizes[file_id] = (space[0], file_positions_sizes[file_id][1])
            break

print(get_checksum(filesystem))