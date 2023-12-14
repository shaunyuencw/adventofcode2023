import time

def transpose_matrix(matrix):
    """ Transpose a matrix represented as a list of strings. """
    return [''.join(row[i] for row in matrix) for i in range(len(matrix[0]))]

def rotate_matrix(matrix, direction, reverse=False):
    if direction == 'north':
        return transpose_matrix(matrix)
    elif direction == 'west':
        return matrix  # No shift for west
    elif direction == 'east':
        return [line[::-1] for line in matrix]
    elif direction == 'south': # Order of operations matters here
        if reverse: 
            return transpose_matrix([line[::-1] for line in matrix])
        else:
            return [line[::-1] for line in transpose_matrix(matrix)]

def tilt_matrix(matrix, direction='north'):
    matrix = rotate_matrix(matrix, direction) # Rotate to tilt direction

    new_matrix = []
    for line in matrix:
        start, count_stone = 0, 0
        new_line = ['.' for _ in range(len(line))] # Set all to nothing first
        for i, char in enumerate(line):
            if char == 'O':
                count_stone += 1
            if char == '#':
                new_line[i] = '#' # Set the barrier
                if count_stone > 0:
                    for j in range(start, start + count_stone): # Push stones to left
                        new_line[j] = 'O'
                start, count_stone = i + 1, 0 # Reset
        
        if count_stone > 0: # If no barrier at the end of the line
            for j in range(start, start + count_stone):
                new_line[j] = 'O'
        new_matrix.append(new_line)

    new_matrix = rotate_matrix(new_matrix, direction, reverse=True) # Rotate back
    return new_matrix

def four_direction_tilt(matrix):
    """ Tilt the matrix in all four directions. """
    for i, direction in enumerate(['north', 'west', 'south', 'east']):
        matrix = tilt_matrix(matrix, direction)
    
    return matrix

def weigh_load(matrix):
    """ Calculate the weight load of a matrix. """
    return sum((len(matrix) - i) * line.count('O') for i, line in enumerate(matrix))

def detect_pattern(sequence, confirmation_repeats=3):
    """ Detects repeating patterns in a sequence. """
    for start in range(len(sequence)):
        for length in range(1, len(sequence) - start):
            pattern = sequence[start:start + length]
            repeats = 0

            for i in range(start + length, len(sequence), length):
                if sequence[i:i + length] == pattern:
                    repeats += 1
                    if repeats >= confirmation_repeats:
                        return start, length
                else:
                    break

    return None, None  # No pattern found

part1, part2 = 0, 0

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

north_tilt = tilt_matrix(matrix)
part1 = weigh_load(north_tilt)

weight_history = []
start_time = time.perf_counter()
total_iterations = 1_000_000_000
for i in range(total_iterations):
    matrix = four_direction_tilt(matrix)
    weight_history.append(weigh_load(matrix))
    if i % 500 == 0 or i == total_iterations - 1:
        start, length = detect_pattern(weight_history)
        if start is not None: # Pattern confirmed 4 times
            print(f"Pattern detected starting at index {start} with a length of {length}")
            break

start = len(weight_history) if start is None else start
length = len(weight_history) if length is None else length

position_in_pattern = (total_iterations - start) % length
part2 = weight_history[start + position_in_pattern - 1]
end_time = time.perf_counter()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}, processed in {round(end_time - start_time, 2)} seconds")