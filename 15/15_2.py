import os

ROBOT = "@"
BOX_L = "["
BOX_R = "]"
WALL = "#"
BLANK = "."

DIRECTIONS = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

#################

def can_move(board: dict[tuple[int, int], str], pos_to_move: list[tuple[int, int]], direction_char: str):
    direction = DIRECTIONS[direction_char]
    for pos in pos_to_move:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if board[next_pos] == WALL:
            return False
    return True

def move(board: dict[tuple[int, int], str], position: tuple[int, int], direction_char: str):
    direction = DIRECTIONS[direction_char]
    pos_to_move = get_tiles_to_move(board, position, direction_char, [])

    if not can_move(board, pos_to_move, direction_char):
        return
    
    if direction_char in ["^", "v"]:
        range_x = (min([pos[0] for pos in pos_to_move]), max([pos[0] for pos in pos_to_move]))
        for col in range(range_x[0], range_x[1] + 1):
            pos_in_col = [pos for pos in pos_to_move if pos[0] == col]
            pos_in_col.sort(key=lambda x: x[1], reverse=direction_char=="^")

            for i in range(len(pos_in_col) - 1, -1, -1):
                next_pos = (pos_in_col[i][0] + direction[0], pos_in_col[i][1] + direction[1])
                board[next_pos] = board[pos_in_col[i]]
                board[pos_in_col[i]] = BLANK
    else:
         pos_to_move.sort(key=lambda x: x[1], reverse=direction_char==">")
         for i in range(len(pos_to_move) - 1, -1, -1):
                next_pos = (pos_to_move[i][0] + direction[0], pos_to_move[i][1] + direction[1])
                board[next_pos] = board[pos_to_move[i]]
                board[pos_to_move[i]] = BLANK

# get all tiles that will move if the inital tile pushes them from the given position in the given direction
def get_tiles_to_move(board: dict[tuple[int, int], str], position: tuple[int, int], direction_char: str, found: list[tuple[int, int]]):
    if position not in found:
        found.append(position)

    direction = DIRECTIONS[direction_char]
    next_pos = (position[0] + direction[0], position[1] + direction[1])

    if board[next_pos] in [BLANK, WALL]:
        return found

    get_tiles_to_move(board, next_pos, direction_char, found)
    
    if board[next_pos] == BOX_L:
        if (next_pos[0] + 1, next_pos[1]) not in found:
            get_tiles_to_move(board, (next_pos[0] + 1, next_pos[1]), direction_char, found)
    elif board[next_pos] == BOX_R:
        if (next_pos[0] - 1, next_pos[1]) not in found:
            get_tiles_to_move(board, (next_pos[0] - 1, next_pos[1]), direction_char, found)

    return found

#################

board = {}
moves = ""

with open("input.txt", "r") as file:
    file_parts = file.read().split("\n\n")
    moves = "".join(file_parts[1].split("\n"))

    map_lines = [line.strip() for line in file_parts[0].split("\n")]
    for y in range(len(map_lines)):
        for x in range(len(map_lines[y])):
            match map_lines[y][x]:
                case "@":
                    board[(x * 2, y)] = ROBOT
                    board[(x * 2 + 1, y)] = BLANK
                case "O":
                    board[(x * 2, y)] = BOX_L
                    board[(x * 2 + 1, y)] = BOX_R
                case ".":
                    board[(x * 2, y)] = BLANK
                    board[(x * 2 + 1, y)] = BLANK
                case "#":
                    board[(x * 2, y)] = WALL
                    board[(x * 2 + 1, y)] = WALL
            
for m in moves:
    for pos, tile in board.items():
        if tile == ROBOT:
            move(board, pos, m)
            break

total = 0
for pos in board:
    if board[pos] != BOX_L:
        continue
    total += pos[0] + (pos[1] * 100)

print(total)