import re

file_content = ""

with open("input.txt", "r") as file:
    file_content = file.read()

instructions = {}

multiplication_instructions = re.finditer(r"mul\(\d+,\d+\)", file_content)
do_instructions = re.finditer(r"do\(\)", file_content)
dont_instructions = re.finditer(r"don't\(\)", file_content)

for instruction in multiplication_instructions:
    instructions[instruction.start()] = instruction.group()

for instruction in do_instructions:
    instructions[instruction.start()] = instruction.group()

for instruction in dont_instructions:
    instructions[instruction.start()] = instruction.group()

instruction_positions = sorted(instructions)
mul_enabled = True
total = 0

for position in instruction_positions:
    instruction = instructions[position]
    
    if instruction == "do()":
        mul_enabled = True
    elif instruction ==  "don't()":
        mul_enabled = False
    else:
        if not mul_enabled:
            continue
        nums = instruction[4:-1].split(",")
        total += int(nums[0]) * int(nums[1])

print(total)