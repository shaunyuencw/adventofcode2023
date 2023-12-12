from itertools import groupby
import time

def count_arrangements(spring_pattern, group_sizes):
    def is_valid_combination(pattern, group_sizes):
        groups = [len(list(g)) for k, g in groupby(pattern) if k == '#'] # Count the number of damaged springs in each group
        return groups == group_sizes # Check if the groups match the required sizes

    stack = [(0, '')]
    valid_combinations = 0

    while stack:
        idx, current_pattern = stack.pop()

        if idx == len(spring_pattern): # Reached the end of the springs pattern
            if is_valid_combination(current_pattern, group_sizes):
                valid_combinations += 1 # Found a valid combination
        else:
            if spring_pattern[idx] == '?': 
                # Try both possibilities for unknown springs
                stack.append((idx + 1, current_pattern + '.')) 
                stack.append((idx + 1, current_pattern + '#'))
            else:
                # Add the current spring to the pattern
                stack.append((idx + 1, current_pattern + spring_pattern[idx]))

    return valid_combinations
rows = []
part1, part2 = 0, 0
with open('input.txt', 'r') as file:
    for line in file:
        springs, arrangements = line.strip().split(' ')
        arrangements = [int(val) for val in arrangements.split(',')]
        
        rows.append((springs, arrangements))

start_time = time.time()
for pattern, group_size in rows:
    #print(pattern, group_size)
    score = count_arrangements(pattern, group_size)
    #print(f"Score: {score}")
    part1 += score
end_time = time.time()

print(f"Part 1: {part1}")
print(f"Proccesed in {round(end_time - start_time, 2)} seconds")
