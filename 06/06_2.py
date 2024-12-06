def get_visited_positions(rows: list[str], obstacles: list[tuple[int, int]], guard_pos: tuple[int, int]):
    guard_direction = (0, -1)
    visited_positions = set()

    while guard_pos[0] in range(len(rows[0])) and guard_pos[1] in range(len(rows)):
        visited_positions.add(guard_pos)

        # turn clockwise 90 degrees if obstacle found
        if (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1]) in obstacles:
            guard_direction = (-guard_direction[1], guard_direction[0])

        guard_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

    return visited_positions

######################

rows = []

with open("input.txt", "r") as file:
    rows = file.readlines()

rows = [row.strip() for row in rows]

# find guard / obstacles
start_guard_pos = (-1, -1)
obstacles = []

for y in range(len(rows)):
    for x in range(len(rows[y])):
        match rows[y][x]:
            case "#":
                obstacles.append((x, y))
            case "^":
                start_guard_pos = (x, y)

guard_pos = start_guard_pos

possible_obstructions = set()
visited_positions = get_visited_positions(rows, obstacles, guard_pos)

for position in visited_positions:
    guard_pos = start_guard_pos
    guard_direction = (0, -1)
    loop_found = False
    
    visited_positions_directions_in_search = set()
    visited_positions_directions_in_search.add((guard_pos, guard_direction))

    altered_obstacles = obstacles.copy()
    altered_obstacles.append(position)

    while not loop_found and guard_pos[0] in range(len(rows[0])) and guard_pos[1] in range(len(rows)):
        next_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

        # turn clockwise 90 degrees if obstacle found
        if next_pos in altered_obstacles:
            guard_direction = (-guard_direction[1], guard_direction[0])
        else:
            guard_pos = next_pos

        if (guard_pos, guard_direction) in visited_positions_directions_in_search:
            possible_obstructions.add(position)
            print(len(possible_obstructions), end="\r")
            loop_found = True
        else:
            visited_positions_directions_in_search.add((guard_pos, guard_direction))

print(len(possible_obstructions))