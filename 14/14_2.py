import os

AREA_WIDTH = 101
AREA_HEIGHT = 103

def move(robot: tuple[tuple[int, int], tuple[int, int]]):
    position = robot[0]
    velocity = robot[1]

    new_position = (position[0] + velocity[0], position[1] + velocity[1])

    # wrap x
    if new_position[0] not in range(AREA_WIDTH):
        if new_position[0] < 0:
            new_position = (AREA_WIDTH + new_position[0], new_position[1])
        else:
            new_position = (new_position[0] - AREA_WIDTH, new_position[1])

    # wrap y
    if new_position[1] not in range(AREA_HEIGHT):
        if new_position[1] < 0:
            new_position = (new_position[0], AREA_HEIGHT + new_position[1])
        else:
            new_position = (new_position[0], new_position[1] - AREA_HEIGHT)
    
    return (new_position, velocity)

def get_robots_in_quadrants(robots: list[tuple[tuple[int, int], tuple[int, int]]]):
    quadrants = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    quadrant = 0
    HALF_WIDTH = AREA_WIDTH // 2
    HALF_HEIGHT = AREA_HEIGHT // 2

    for robot in robots:
        position = robot[0]

        if position[0] == HALF_WIDTH or position[1] == HALF_HEIGHT:
            continue

        if position[0] < HALF_WIDTH and position[1] < HALF_HEIGHT:
            quadrant = 1
        elif position[0] < HALF_WIDTH and position[1] > HALF_HEIGHT:
            quadrant = 2
        elif position[0] > HALF_WIDTH and position[1] < HALF_HEIGHT:
            quadrant = 3
        else:
            quadrant = 4

        quadrants[quadrant] += 1

    return quadrants

def text_color(r: int = 0, g: int = 0, b: int = 0, background: bool = False, reset: bool = False) -> str:
    if reset:
        return "\033[0m"
    else:
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def render_robots(robots: list[tuple[tuple[int, int], tuple[int, int]]], move_count: int):
    print("\033[0;0H")  # move cursor to start
    positions = [robot[0] for robot in robots]
    
    for y in range(0, AREA_HEIGHT, 2):
        for x in range(AREA_WIDTH):
            fg = text_color(255, 255, 255) if (x, y) in positions else text_color(0, 0, 0)
            bg = text_color(255, 255, 255, background=True) if (x, y + 1) in positions else text_color(0, 0, 0, background=True)
            print(f"{fg}{bg}▀{text_color(reset=True)}", end="")
        print()
    print(move_count)

##################

# stored as (position tuple, velocity tuple)
robots = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        position = line.split(" ")[0][2:].split(",")
        p_x = int(position[0])
        p_y = int(position[1])
        
        velocity = line.split(" ")[1][2:].split(",")
        v_x = int(velocity[0])
        v_y = int(velocity[1])

        robots.append(((p_x, p_y), (v_x, v_y)))

# just let it go until we see a christmas tree i guess??????
# this part is so stupid
counter = 0
render_robots(robots, 0)

while True:
    counter += 1
    for j in range(len(robots)):
        robots[j] = move(robots[j])
    render_robots(robots, counter)