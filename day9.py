from collections import deque

with open('day9.txt') as f:
    puzzle_input = [[int(y) for y in x.strip()] for x in f.readlines()]


def get_low_points(lines):
    low_points = []

    for i, y in enumerate(lines):
        for j, x in enumerate(y):
            if i > 0:
                up = lines[i - 1][j]
            else:
                up = 10

            if i < len(lines) - 1:
                down = lines[i + 1][j]
            else:
                down = 10

            if j < len(y) - 1:
                right = lines[i][j + 1]
            else:
                right = 10

            if j > 0:
                left = lines[i][j - 1]
            else:
                left = 10

            if x < up and x < down and x < left and x < right:
                low_points.append((i, j))

    return low_points


def part_1(lines):
    low_points = get_low_points(lines)

    return sum([1 + lines[low_point[0]][low_point[1]] for low_point in low_points])


print(part_1(puzzle_input))
