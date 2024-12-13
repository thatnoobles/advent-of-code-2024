def in_bounds(garden: list[str], pos: tuple[int, int]):
    return pos[0] in range(len(garden[0])) and pos[1] in range(len(garden))

def get_contiguous_tiles(garden: list[str], pos: tuple[int, int], found: set[tuple[int, int]]):
    found.add(pos)
    direction = (-1, 0)

    for _ in range(4):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if in_bounds(garden, next_pos) and next_pos not in found and garden[pos[1]][pos[0]] == garden[next_pos[1]][next_pos[0]]:
            get_contiguous_tiles(garden, next_pos, found)
        direction = (-direction[1], direction[0])
    return found

def get_perimeter(area: set[tuple[int, int]]):
    perimeter = 0

    for pos in area:
        direction = (-1, 0)

        for _ in range(4):
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])

            if next_pos not in area:
                perimeter += 1
            direction = (-direction[1], direction[0])
    return perimeter

####################

garden = []

with open("input.txt", "r") as file:
    garden = [line.strip() for line in file.readlines()]

found_areas = []

for y in range(len(garden)):
    for x in range(len(garden[y])):
        area = get_contiguous_tiles(garden, (x, y), set())
        
        if (garden[y][x], area) not in found_areas:
            found_areas.append((garden[y][x], area))

cost = 0

for found_area in found_areas:
    perimeter = get_perimeter(found_area[1])
    area = len(found_area[1])
    cost += area * perimeter

print(cost)