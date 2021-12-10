with open('day10.txt') as f:
    puzzle_input = [x.strip() for x in f.readlines()]


opening_chunks = ["(", "{", "[", "<"]
matching_closing_chunk = {"(": ")", "{": "}", "[": "]", "<": ">"}


def is_line_illegal(last_opened_chunk, char):
    if matching_closing_chunk.get(last_opened_chunk) != char:
        return True

    return False


def part_1(lines):
    illegal_characters = []
    illegal_chunk_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in lines:
        open_chunks = []
        for char in line:
            if char in opening_chunks:
                open_chunks.append(char)
            else:
                if is_line_illegal(open_chunks[-1], char):
                    illegal_characters.append(char)
                    break
                else:
                    open_chunks.pop()

    total = 0
    for char in illegal_characters:
        total += illegal_chunk_scores.get(char)

    return total


def part_2(lines):
    incomplete_line_scores = []
    closing_chunk_scores = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in lines:
        open_chunks = []
        current_line_legal = True

        for char in line:
            if char in opening_chunks:
                open_chunks.append(char)
            else:
                if is_line_illegal(open_chunks[-1], char):
                    current_line_legal = False
                    break
                else:
                    open_chunks.pop()

        if current_line_legal:
            score_for_line = 0
            for chunk in reversed(open_chunks):
                closing_chunk = matching_closing_chunk.get(chunk)
                score_for_line *= 5
                score_for_line += closing_chunk_scores.get(closing_chunk)

            incomplete_line_scores.append(score_for_line)

    incomplete_line_scores = sorted(incomplete_line_scores)
    return incomplete_line_scores[len(incomplete_line_scores) // 2]


print(part_1(puzzle_input))
print(part_2(puzzle_input))
