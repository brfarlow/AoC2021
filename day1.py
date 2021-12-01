with open('day1.txt') as f:
    puzzle_input = [int(x) for x in f.readlines()]


def part_1(lines):
    times_increased = 0
    current_depth = lines[0]

    for i in range(1, len(lines)):
        if lines[i] > current_depth:
            times_increased += 1

        current_depth = lines[i]

    return times_increased


def part_2(lines):
    times_increased = 0
    current_depth = sum(lines[:3])

    for i in range(1, len(lines)):
        next_depth = sum(lines[i:i+3])
        if next_depth > current_depth:
            times_increased += 1

        current_depth = next_depth

    return times_increased


print(part_1(puzzle_input))
print(part_2(puzzle_input))
