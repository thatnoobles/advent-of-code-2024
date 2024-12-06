# turns should have 3 elements in it
def get_fourth_turn(turns: list[tuple[int, int]], guard_direction: tuple[int, int]):
    if guard_direction[0] == 0:  # x direction 0 = vertical
        return (turns[2][0], turns[0][1])
    elif guard_direction[1] == 0:  # y direction 0 = horizontal
        return (turns[0][0], turns[2][1])
    else:  # invalid direction - can't move diagonally
        return (-1, -1)
    
def path_clear(rows: list[str], start: tuple[int, int], end: tuple[int, int], direction: tuple[int, int]):
    if direction[0] == 0:  # x direction 0 = vertical
        for i in range(start[1], end[1], direction[1]):
            if rows[i][start[0]] == "#":
                return False
        return True
    elif direction[1] == 0:  # y direction 0 = horizontal
        for i in range(start[0], end[0], direction[0]):
            if rows[start[1]][i] == "#":
                return False
        return True
    else: # invalid direction - can't move diagonally
        return False

####################

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

# traverse board, this time also tracking most recent three turns
# if remaining fourth turn (to complete the square) is a position the guard would've visited, we can place an obstruction there
# otherwise turning in such a way that we pass through the start point would also be a loop
guard_start_pos = guard_pos
visited_positions = set()
recent_turns = []
possible_obstructions = []

while guard_pos[0] in range(len(rows[0])) and guard_pos[1] in range(len(rows)):
    visited_positions.add(guard_pos)

    # turn clockwise 90 degrees if obstacle found
    if (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1]) in obstacles:
        guard_direction = (-guard_direction[1], guard_direction[0])
        recent_turns.append(guard_pos)

    if len(recent_turns) == 3:
        fourth_turn = get_fourth_turn(recent_turns, guard_direction)

        if fourth_turn in visited_positions and path_clear(rows, guard_pos, fourth_turn, guard_direction):
            possible_obstructions.append((fourth_turn[0] + guard_direction[0], fourth_turn[1] + guard_direction[1]))

        recent_turns.pop(0)

    guard_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

    if guard_pos[0] == guard_start_pos[0] and guard_pos[1] > guard_start_pos[1] and guard_direction == (-1, 0):
        possible_obstructions.append((guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1]))

print(possible_obstructions)