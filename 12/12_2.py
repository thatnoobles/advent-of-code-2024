def in_bounds(garden: list[str], pos: tuple[int, int]):
    return pos[0] in range(len(garden[0])) and pos[1] in range(len(garden))

def get_contiguous_tiles_by_grid(garden: list[str], pos: tuple[int, int], found: set[tuple[int, int]]):
    found.add(pos)
    direction = (-1, 0)

    for _ in range(4):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if in_bounds(garden, next_pos) and next_pos not in found and garden[next_pos[1]][next_pos[0]] == garden[pos[1]][pos[0]]:
            get_contiguous_tiles_by_grid(garden, next_pos, found)
        direction = (-direction[1], direction[0])
    return found

def get_contiguous_tiles_by_area(tiles: set[tuple[int, int]], pos: tuple[int, int], found: set[tuple[int, int]]):
    found.add(pos)
    direction = (-1, 0)

    for _ in range(4):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        if next_pos in tiles and next_pos not in found:
            get_contiguous_tiles_by_area(tiles, next_pos, found)
        direction = (-direction[1], direction[0])
    return found

def get_sides(area: set[tuple[int, int]]):
    perimeter_directions = {}
    
    direction = (-1, 0)
    for _ in range(4):
        for pos in area:
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if next_pos not in area:
                if direction not in perimeter_directions:
                    perimeter_directions[direction] = set()
                perimeter_directions[direction].add(pos)

        direction = (-direction[1], direction[0])

    side_count = 0
    for direction in perimeter_directions:
        sides = []

        for pos in perimeter_directions[direction]:
            area = get_contiguous_tiles_by_area(perimeter_directions[direction], pos, set())

            if area not in sides:
                sides.append(area)
        side_count += len(sides)

    return side_count

#############

garden = []

with open("input.txt", "r") as file:
    garden = [line.strip() for line in file.readlines()]

found_areas = []

for y in range(len(garden)):
    for x in range(len(garden[y])):
        area = get_contiguous_tiles_by_grid(garden, (x, y), set())
        if (garden[y][x], area) not in found_areas:
            found_areas.append((garden[y][x], area))

cost = 0

for area in found_areas:
    sides = get_sides(area[1])
    cost += len(area[1]) * sides

print(cost)