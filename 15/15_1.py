ROBOT = "@"
BOX = "O"
WALL = "#"
BLANK = "."

DIRECTIONS = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

#################

def can_move(board: dict[tuple[int, int], str], position: tuple[int, int], direction_char: str):
    direction = DIRECTIONS[direction_char]
    next_pos = (position[0] + direction[0], position[1] + direction[1])

    if board[next_pos] == WALL:
        return False
    elif board[next_pos] == BLANK:
        return True
    else:
        return can_move(board, next_pos, direction_char)
    
def move(board: dict[tuple[int, int], str], position: tuple[int, int], direction_char: str):
    direction = DIRECTIONS[direction_char]
    next_pos = (position[0] + direction[0], position[1] + direction[1])

    board[next_pos] = board[position]
    board[position] = BLANK

def move_and_push(board: dict[tuple[int, int], str], position: tuple[int, int], direction_char: str):
    if not can_move(board, position, direction_char):
        return False

    direction = DIRECTIONS[direction_char]
    
    # get boxes that need to be pushed
    iter_pos = (position[0] + direction[0], position[1] + direction[1])
    box_positions = []

    while board[iter_pos] != BLANK:
        box_positions.append(iter_pos)
        iter_pos = (iter_pos[0] + direction[0], iter_pos[1] + direction[1])

    for i in range(len(box_positions) - 1, -1, -1):
        move(board, box_positions[i], direction_char)

    move(board, position, direction_char)

#################

board = {}
moves = ""

with open("input.txt", "r") as file:
    file_parts = file.read().split("\n\n")
    moves = "".join(file_parts[1].split("\n"))

    map_lines = [line.strip() for line in file_parts[0].split("\n")]
    for y in range(len(map_lines)):
        for x in range(len(map_lines[y])):
            board[(x, y)] = map_lines[y][x]

for m in moves:
    for pos, tile in board.items():
        if tile == ROBOT:
            move_and_push(board, pos, m)
            break

total = 0
for pos in board:
    if board[pos] != BOX:
        continue
    total += pos[0] + (pos[1] * 100)

print(total)