from collections import Counter

with open('day6.txt') as f:
    state = [int(x) for x in f.read().split(',')]


def process_lifecycle(initial_state, days_to_process):
    days_in_cycle = Counter(initial_state)
    for _ in range(days_to_process):
        next_day = Counter()
        for day, number_of_fish in days_in_cycle.items():
            if day == 0:
                next_day[6] += number_of_fish
                next_day[8] += number_of_fish
            else:
                next_day[day - 1] += number_of_fish

        days_in_cycle = next_day

    return sum(days_in_cycle.values())


print(process_lifecycle(state, 18))
print(process_lifecycle(state, 256))
