# tuples are (x, y)
def search(rows: list[str], start_position: tuple[int, int]) -> bool:
    # check bounds
    for i in range(-1, 2):
        if start_position[0] + i not in range(len(rows[0])) or start_position[1] + i not in range(len(rows)):
            return False
        
    upper_letters = (rows[start_position[1] - 1][start_position[0] - 1], rows[start_position[1] - 1][start_position[0] + 1])
    lower_letters = (rows[start_position[1] + 1][start_position[0] - 1], rows[start_position[1] + 1][start_position[0] + 1])
    
    # ough
    if upper_letters in [("S", "M"), ("M", "S")]:
        return upper_letters == lower_letters
    elif upper_letters == ("S", "S"):
        return lower_letters == ("M", "M")
    elif upper_letters == ("M", "M"):
        return lower_letters == ("S", "S")
    else:
        return False

###################

rows = []
found_count = 0

with open("input.txt", "r") as file:
    rows = [line.strip() for line in file.readlines()]

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == "A" and search(rows, (x, y)):
            found_count += 1

print(found_count)
