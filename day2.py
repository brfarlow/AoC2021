with open('day2.txt') as f:
    puzzle_input = [x.split() for x in f.readlines()]


def part_1(lines):
    horizontal_position = 0
    depth = 0

    for i in lines:
        direction = i[0]
        distance = int(i[1])

        if direction == "forward":
            horizontal_position += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    return depth * horizontal_position


def part_2(lines):
    horizontal_position = 0
    depth = 0
    aim = 0

    for i in lines:
        direction = i[0]
        distance = int(i[1])

        if direction == "forward":
            horizontal_position += distance
            depth += (aim * distance)
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    return depth * horizontal_position


print(part_1(puzzle_input))
print(part_2(puzzle_input))
