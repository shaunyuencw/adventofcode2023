def is_row_symmetric(puzzle, row_index, is_part_two=False):
    # Determine the number of rows to compare on each side of row_index
    num_rows_to_compare = min(row_index, len(puzzle) - row_index)

    # Select the appropriate range of rows above and below row_index
    upper_rows = puzzle[row_index - num_rows_to_compare : row_index]
    lower_rows = puzzle[row_index: row_index + num_rows_to_compare]

    if is_part_two:
        return is_smudged(upper_rows[::-1], lower_rows)
    
    return upper_rows[::-1] == lower_rows if num_rows_to_compare > 0 else False

def transpose_matrix(matrix):
    """ Transpose a matrix represented as a list of strings. """
    return [''.join(row[i] for row in matrix) for i in range(len(matrix[0]))]

def is_smudged(matrix1, matrix2):
    # Count differences
    diff_count = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                diff_count += 1
                if diff_count > 1:
                    return False
                
    return diff_count == 1
        
puzzles = []
with open('input.txt', 'r') as file:
    temp_puzzle = []
    for line in file:
        # Save puzzle if line is empty
        if line == '\n':
            puzzles.append(temp_puzzle)
            temp_puzzle = []
        else:
            temp_puzzle.append(line.strip())

    puzzles.append(temp_puzzle) # Last puzzle

part1, part2 = 0, 0
for i, puzzle in enumerate(puzzles):
    part1_found, part2_found = False, False
    transposed_puzzle = transpose_matrix(puzzle)
    for row_index in range(1, len(puzzle)):
        if is_row_symmetric(puzzle, row_index):
            part1 += row_index * 100
            part1_found = True

        if is_row_symmetric(puzzle, row_index, is_part_two=True):
            part2 += row_index * 100
            part2_found = True

        if part1_found and part2_found:
            break

    for col_index in range(1, len(transposed_puzzle)):
        if is_row_symmetric(transposed_puzzle, col_index):
            part1 += col_index
            part1_found = True
            
        if is_row_symmetric(transposed_puzzle, col_index, is_part_two=True):
            part2 += col_index
            part2_found = True

        if part1_found and part2_found:
            break
        
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")