def in_bounds(topo_map: list[list[int]], position: tuple[int, int]):
    return position[0] in range(len(topo_map[0])) and position[1] in range(len(topo_map))

def get_positions(topo_map: list[list[int]], height: int):
    result = []

    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[y][x] == height:
                result.append((x, y))
    return result

# returns positions of neighboring heights if they are + 1 of current height
def get_adjacent_positions(topo_map: list[list[int]], current_position: tuple[int, int]):
    result = []

    x = current_position[0]
    y = current_position[1]
    next_height = topo_map[y][x] + 1

    direction = (0, 1)
    for _ in range(4):
        next_position = (x + direction[0], y + direction[1])

        if in_bounds(topo_map, next_position) and topo_map[next_position[1]][next_position[0]] == next_height:
            result.append((next_position))
        direction = (-direction[1], direction[0])

    return result

def calculate_reachable_maximums(topo_map: list[list[int]], position: tuple[int, int]):
    x = position[0]
    y = position[1]
    if topo_map[y][x] == 9:
        result = set()
        result.add((x, y))
        return result
    
    next_positions = get_adjacent_positions(topo_map, position)
    reachable_maximums = set()

    for pos in next_positions:
        reachable_maximums = reachable_maximums.union(calculate_reachable_maximums(topo_map, pos))
    return reachable_maximums

####################

topo_map = []

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        topo_map.append([int(i) if i != "." else -1 for i in line])

total_score = 0
trailheads = get_positions(topo_map, 0)

for trailhead_position in trailheads:
    score = len(calculate_reachable_maximums(topo_map, trailhead_position))
    total_score += score

print(total_score)