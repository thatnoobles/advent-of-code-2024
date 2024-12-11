import functools

@functools.cache
def get_resulting_stone_count(stone: int, blinks: int):
    if blinks == 0:
        return 1

    if stone == 0:
        return get_resulting_stone_count(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_1 = int(stone_str[:len(stone_str) // 2])
        stone_2 = int(stone_str[len(stone_str) // 2:])
        return get_resulting_stone_count(stone_1, blinks - 1) + get_resulting_stone_count(stone_2, blinks - 1)
    else:
        return get_resulting_stone_count(stone * 2024, blinks - 1)

###########################

stones = []

with open("input.txt", "r") as file:
    stones = [int(i) for i in file.read().strip().split(" ")]

count = 0

for stone in stones:
    count += get_resulting_stone_count(stone, 75)

print(count)