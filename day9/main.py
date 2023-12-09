def process_pattern(pattern):
    differences = pattern
    prev_patterns = []
    while True:
        differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)] # Differences between consecutive elements

        if all(value == 0 for value in differences):
            break # Sequence is all zeros
        prev_patterns.append(differences)

    next_increment, prev_increment = 0, 0
    for pattern_id in range(len(prev_patterns) - 1, -1, -1):
        next_increment += prev_patterns[pattern_id][-1] # Add the last value of the current pattern to next_increment
        prev_increment = prev_patterns[pattern_id][0] - prev_increment # Calculate prev_increment as the first value of the current pattern minus the existing prev_increment

    return pattern[-1] + next_increment, pattern[0] - prev_increment # Return the next value and the past value

part1, part2 = 0, 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pattern = [int(val) for val in line.split()]
        next_value, past_value = process_pattern(pattern)
        # print(f"{past_value=}, {pattern=}, {next_value=}") # If you want to visualize the process

        part1 += next_value
        part2 += past_value

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
