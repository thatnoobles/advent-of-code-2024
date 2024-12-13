import numpy as np

SMALL_DECIMAL_NUMBER = 0.00000001

def solve(config: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]):
    button_a = config[0]
    button_b = config[1]
    prize = config[2]

    a = np.array([[button_a[0], button_b[0]], [button_a[1], button_b[1]]])
    b = np.array(list(prize))
    solution = np.linalg.solve(a, b)
    return solution

def solution_is_valid(a: float, b: float):
    return abs(round(a) - a) < SMALL_DECIMAL_NUMBER and abs(round(b) - b) < SMALL_DECIMAL_NUMBER

###################

# stored as tuple (button A, button B, prize)
configs = []

with open("input.txt", "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 4):
        a = (int(lines[i].split(": ")[1].split(", ")[0][2:]), int(lines[i].split(": ")[1].split(", ")[1][2:]))
        b = (int(lines[i + 1].split(": ")[1].split(", ")[0][2:]), int(lines[i + 1].split(": ")[1].split(", ")[1][2:]))
        prize = (int(lines[i + 2].split(": ")[1].split(", ")[0][2:]), int(lines[i + 2].split(": ")[1].split(", ")[1][2:]))
        configs.append((a, b, prize))

cost = 0

for config in configs:
    solution = solve(config)
    a = solution[0]  # num presses
    b = solution[1]

    if solution_is_valid(a, b) and round(a) in range(101) and round(b) in range(101):
        cost += (3 * round(a)) + round(b)

print(cost)