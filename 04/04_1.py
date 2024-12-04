# tuples are (x, y)
def search(rows: list[str], start_position: tuple[int, int], letter: str, direction: tuple[int, int]) -> bool:
    next_position = (start_position[0] + direction[0], start_position[1] + direction[1])

    # next position would go out-of-bounds
    if next_position[0] not in range(len(rows[0])) or next_position[1] not in range(len(rows)):
        return False
    
    if rows[next_position[1]][next_position[0]] == letter:
        match letter:
            case "M":
                return search(rows, next_position, "A", direction)
            case "A":
                return search(rows, next_position, "S", direction)
            case _:
                return True
            
    return False

###################

rows = []
found_count = 0

with open("input.txt", "r") as file:
    rows = [line.strip() for line in file.readlines()]

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == "X":
            for direction_x in range(-1, 2):
                for direction_y in range(-1, 2):
                    if search(rows, (x, y), "M", (direction_x, direction_y)):
                        found_count += 1

print(found_count)
