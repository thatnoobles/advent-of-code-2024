rows = []

with open("input.txt", "r") as file:
    rows = file.readlines()

rows = [row.strip() for row in rows]

# find guard / obstacles
guard_direction = (0, -1)
guard_pos = (-1, -1)
obstacles = []

for y in range(len(rows)):
    for x in range(len(rows[y])):
        match rows[y][x]:
            case "#":
                obstacles.append((x, y))
            case "^":
                guard_pos = (x, y)

visited_positions = set()

while guard_pos[0] in range(len(rows[0])) and guard_pos[1] in range(len(rows)):
    visited_positions.add(guard_pos)

    # turn clockwise 90 degrees if obstacle found
    if (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1]) in obstacles:
        guard_direction = (-guard_direction[1], guard_direction[0])

    guard_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

print(len(visited_positions))