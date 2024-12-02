left = []
right = []
lines = []

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    split = line.split("   ")
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()

total_distance = 0

for i in range(len(left)):
    total_distance += abs(left[i] - right[i])

print(total_distance)