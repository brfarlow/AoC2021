def get_length_of_different_segments(first, second):
    first_set, second_set = set(first), set(second)
    return len((first_set | second_set) - (first_set & second_set))


def get_length_of_same_segments(first, second):
    return len(set(first) & set(second))


def part_1(puzzle_input):
    times_unique_number_segment_seen = 0
    for line in puzzle_input:
        for number in line[1]:
            if len(number) in [2, 3, 4, 7]:
                times_unique_number_segment_seen += 1

    return times_unique_number_segment_seen


def part_2(puzzle_input):
    total_output_value = 0
    codes = {}

    for line in puzzle_input:
        for segment in line[0]:
            if len(segment) == 2:
                codes[1] = segment
            elif len(segment) == 3:
                codes[7] = segment
            elif len(segment) == 4:
                codes[4] = segment
            elif len(segment) == 7:
                codes[8] = segment

        for segment in line[0]:
            if len(segment) == 5:
                if get_length_of_different_segments(codes[1], segment) == 3:
                    codes[3] = segment
                elif get_length_of_different_segments(codes[4], segment) == 3:
                    codes[5] = segment
                else:
                    codes[2] = segment
            elif len(segment) == 6:
                if get_length_of_same_segments(codes[1], segment) == 1:
                    codes[6] = segment
                elif get_length_of_same_segments(codes[4], segment) == 4:
                    codes[9] = segment
                else:
                    codes[0] = segment

        reversed_codes = {value: str(key) for key, value in codes.items()}
        total_output_value += int(''.join([reversed_codes[output] for output in line[1]]))

    return total_output_value


def main():
    with open('day8.txt') as f:
        puzzle_input = []
        for x in f.readlines():
            segments, output = x.strip().split('|')
            segments = list(map(''.join, map(sorted, segments.split())))
            output = list(map(''.join, map(sorted, output.split())))
            puzzle_input.append((segments, output))

    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == main():
    main()
