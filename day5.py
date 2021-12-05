from copy import deepcopy


def part_1(puzzle_input, grid):
    for line in puzzle_input:
        if line[0][1] == line[1][1]:
            for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                grid[line[0][1]][i] += 1
        elif line[0][0] == line[1][0]:
            for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                grid[i][line[0][0]] += 1

    greater_than_two_times_seen = 0
    for line in grid:
        for num in line:
            if num > 1:
                greater_than_two_times_seen += 1

    return greater_than_two_times_seen


def part_2(puzzle_input, grid):
    for line in puzzle_input:
        if line[0][1] == line[1][1]:
            for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                grid[line[0][1]][i] += 1
        elif line[0][0] == line[1][0]:
            for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                grid[i][line[0][0]] += 1
        else:
            min_x = min(line[0][0], line[1][0])
            max_x = max(line[0][0], line[1][0])

            if line[0][0] > line[1][0]:
                min_y = line[1][1]
                max_y = line[0][1]
            else:
                min_y = line[0][1]
                max_y = line[1][1]

            slope = min_y
            for i in range(min_x, max_x + 1):
                grid[slope][i] += 1
                if max_y > min_y:
                    slope += 1
                else:
                    slope -= 1

    greater_than_two_times_seen = 0
    for line in grid:
        for num in line:
            if num > 1:
                greater_than_two_times_seen += 1

    return greater_than_two_times_seen


def main():
    with open('day5.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    puzzle_input = []
    for line in lines:
        start, end = line.split('->')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        puzzle_input.append([(int(start_x), int(start_y)), (int(end_x), int(end_y))])

    # find max x dimension to make a x,y grid
    x = 0
    for line in puzzle_input:
        if max(line[0]) > x or max(line[1]) > x:
            x = [max(line[0]), max(line[1])][max(line[0]) < max(line[1])]

    grid = [[0 for _ in range(x + 1)] for _ in range(x + 1)]
    part_2_grid = deepcopy(grid)
    print(part_1(puzzle_input, grid))
    print(part_2(puzzle_input, part_2_grid))


if __name__ == '__main__':
    main()
