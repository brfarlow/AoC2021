with open('day7.txt') as f:
    puzzle_input = [int(x) for x in f.read().split(',')]

# puzzle_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def part_1(crabs):
    min_pos, max_pos = min(crabs), max(crabs)
    least_full_used, position_of_least_full_used = None, None

    for i in range(min_pos, max_pos + 1):
        total_fuel_used = sum(abs(crab - i) for crab in crabs)

        if least_full_used is None or total_fuel_used < least_full_used:
            least_full_used = total_fuel_used

    return least_full_used


def part_2(crabs):
    min_pos, max_pos = min(crabs), max(crabs)
    least_full_used = None

    for i in range(min_pos, max_pos + 1):
        total_fuel_used = sum((abs(crab - i) * (1 + abs(crab - i))) // 2 for crab in crabs)

        if least_full_used is None or total_fuel_used < least_full_used:
            least_full_used = total_fuel_used

    return least_full_used


print(part_1(puzzle_input))
print(part_2(puzzle_input))
