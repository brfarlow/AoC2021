with open('day3.txt') as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def part_1(lines):
    gamma_rate = list(lines[0])
    epsilon_rate = list(lines[0])
    length = len(lines[0])

    for bit in range(length):
        bits = [x[bit] for x in lines]
        if bits.count('1') > bits.count('0'):
            gamma_rate[bit] = '1'
            epsilon_rate[bit] = '0'
        else:
            gamma_rate[bit] = '0'
            epsilon_rate[bit] = '1'

    return int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2)


def part2(lines):
    oxygen_rating = lines
    carbon_rating = oxygen_rating.copy()
    length = len(lines[0])

    for bit in range(length):
        oxygen_bits = [x[bit] for x in oxygen_rating]

        if oxygen_bits.count('1') >= oxygen_bits.count('0'):
            oxygen_rating = [x for x in oxygen_rating if x[bit] == '1']
        else:
            oxygen_rating = [x for x in oxygen_rating if x[bit] == '0']

        if len(oxygen_rating) == 1:
            break

    for bit in range(len(carbon_rating[0])):
        carbon_bits = [x[bit] for x in carbon_rating]

        if carbon_bits.count('1') >= carbon_bits.count('0'):
            carbon_rating = [x for x in carbon_rating if x[bit] == '0']
        else:
            carbon_rating = [x for x in carbon_rating if x[bit] == '1']

        if len(carbon_rating) == 1:
            break

    return int(oxygen_rating[0], 2) * int(carbon_rating[0], 2)


print(part_1(puzzle_input))
print(part2(puzzle_input))
