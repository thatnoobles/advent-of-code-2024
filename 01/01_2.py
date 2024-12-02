left = []
right = []
lines = []

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    split = line.split("   ")
    left.append(int(split[0]))
    right.append(int(split[1]))

similarity_score = 0

for num_left in left:
    count = 0

    for num_right in right:
        if num_right == num_left:
            count += 1
    
    similarity_score += num_left * count

print(similarity_score)