import itertools

# operators should have one less element than values
def solve(values: list[int], operators: tuple[str, ...]):
    total = values[0]

    for i in range(1, len(values)):
        match operators[i - 1]:
            case "+":
                total += values[i]
            case "*":
                total *= values[i]
    return total

def solvable(target: int, values: list[int]):
    possible_operators = itertools.product("*+", repeat=len(values) - 1)
    
    for operators in possible_operators:
        if solve(values, operators) == target:
            return True

####################

equations = []
total = 0

with open("input.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        equations.append((int(line.split(":")[0]), [int(num.strip()) for num in line.strip().split(":")[1].split(" ")[1:]]))

for equation in equations:
    if solvable(equation[0], equation[1]):
        total += equation[0]

print(total)