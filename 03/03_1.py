import re

file_content = ""

with open("input.txt", "r") as file:
    file_content = file.read()

matching_instructions = re.findall(r"mul\(\d+,\d+\)", file_content)
total = 0

for instruction in matching_instructions:
    nums = instruction[4:-1].split(",")
    total += int(nums[0]) * int(nums[1])

print(total)