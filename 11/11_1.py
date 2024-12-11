def blink(stones: list[int]):
    result = []

    for stone in stones:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            result.append(int(stone_str[:len(stone_str) // 2]))
            result.append(int(stone_str[len(stone_str) // 2:]))
        else:
            result.append(stone * 2024)
    return result

###########################

stones = []

with open("input.txt", "r") as file:
    stones = [int(i) for i in file.read().strip().split(" ")]

for _ in range(25):
    stones = blink(stones)

print(len(stones))