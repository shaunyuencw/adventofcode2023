import time

def count_arrangements(springs_pattern, damaged_group_sizes, current_pos, current_block_index, current_block_length, memo):
    """
    Recursively counts the number of valid arrangements of springs (both operational and damaged)
    according to the given pattern and group sizes, using memoization to optimize performance.
    """

    # Key for memoization to avoid recalculating the same state
    state_key = (current_pos, current_block_index, current_block_length)
    if state_key in memo:
        return memo[state_key]

    # Base case: reached the end of the springs pattern
    if current_pos == len(springs_pattern):
        # Check if all blocks are accounted for and the current block length matches the required size
        if current_block_index == len(damaged_group_sizes) and current_block_length == 0:
            return 1
        elif current_block_index == len(damaged_group_sizes) - 1 and damaged_group_sizes[current_block_index] == current_block_length:
            return 1
        else:
            return 0

    # Count the number of valid arrangements
    arrangements_count = 0
    for spring_state in ['.', '#']:
        # Check if the current position matches the spring state or is unknown
        if springs_pattern[current_pos] == spring_state or springs_pattern[current_pos] == '?':
            # Handle operational spring
            if spring_state == '.' and current_block_length == 0:
                arrangements_count += count_arrangements(springs_pattern, damaged_group_sizes, current_pos + 1, current_block_index, 0, memo)
            # Handle operational spring, completing a block of damaged springs
            elif spring_state == '.' and current_block_length > 0 and current_block_index < len(damaged_group_sizes) and damaged_group_sizes[current_block_index] == current_block_length:
                arrangements_count += count_arrangements(springs_pattern, damaged_group_sizes, current_pos + 1, current_block_index + 1, 0, memo)
            # Handle damaged spring
            elif spring_state == '#':
                arrangements_count += count_arrangements(springs_pattern, damaged_group_sizes, current_pos + 1, current_block_index, current_block_length + 1, memo)
    
    # Store the result in the memo dictionary
    memo[state_key] = arrangements_count
    return arrangements_count


rows = []
part1, part2 = 0,0

with open('input.txt', 'r') as file:
    for line in file:
        springs, arrangements = line.strip().split(' ')
        arrangements = [int(val) for val in arrangements.split(',')]
        rows.append((springs, arrangements))

start_time = time.time()
for pattern, group_size in rows:
    DP = {} # Clearing the memoization dictionary
    score = count_arrangements(pattern, group_size, 0, 0, 0, DP)
    part1 += score

    # Part 2
    pattern_p2 = '?'.join([pattern] * 5)
    group_size_p2 = group_size * 5

    DP = {} # Clearing the memoization dictionary
    score = count_arrangements(pattern_p2, group_size_p2, 0, 0, 0, DP)
    part2 += score
end_time = time.time()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
print(f"Processed in {round(end_time - start_time, 2)} seconds")