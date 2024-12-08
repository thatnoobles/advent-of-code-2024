import itertools

def get_antinodes(antenna_1: tuple[int, int], antenna_2: tuple[int, int], bounds: tuple[int, int]):
    distance = (antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1])
    
    antinodes = [antenna_1, antenna_2]

    antinode_pos = antenna_1

    while antinode_pos[0] in range(bounds[0]) and antinode_pos[1] in range(bounds[1]):
        antinode_pos = (antinode_pos[0] - distance[0], antinode_pos[1] - distance[1])
        antinodes.append(antinode_pos)

    while antinode_pos[0] in range(bounds[0]) and antinode_pos[1] in range(bounds[1]):
        antinode_pos = (antinode_pos[0] + distance[0], antinode_pos[1] + distance[1])
        antinodes.append(antinode_pos)

    return antinodes

def get_all_antinodes(antennas: dict[str, list[tuple[int, int]]], frequency: str, bounds: tuple[int, int]):
    result = set()

    possible_antenna_combinations = list(itertools.product(antennas[frequency], repeat=2))

    for antenna_duo in possible_antenna_combinations:
        if antenna_duo[0] == antenna_duo[1]:
            continue
            
        antinodes = get_antinodes(antenna_duo[0], antenna_duo[1], bounds)
        for antinode in antinodes:
            result.add(antinode)

    return result

########################

antennas: dict[str, list[tuple[int, int]]] = {}
total_antinodes = set()
area_size = tuple()

with open("input.txt", "r") as file:
    lines = file.readlines()
    area_size = (len(lines[0].strip()), len(lines))

    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            tile = lines[y][x]

            if tile == ".":
                continue
            if tile not in antennas:
                antennas[tile] = []
            antennas[tile].append((x, y))

for frequency in antennas:
    antinodes = get_all_antinodes(antennas, frequency, area_size)
    
    for antinode in antinodes:
        if antinode[0] in range(area_size[0]) and antinode[1] in range(area_size[1]):
            total_antinodes.add(antinode)

print(len(total_antinodes))