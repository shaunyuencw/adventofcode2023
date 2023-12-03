def append_gear(key, value):
    potential_gears.setdefault(key, []).append(value)

def check_number_and_find_gear(matrix, start_row, start_col, end_col):
    rows = len(matrix)
    cols = len(matrix[0])
    isValid = False
    potentialGear = None

    adjacent_positions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top left, Top, Top right
        (0, -1),           (0, 1),   # Left,       , Right
        (1, -1),  (1, 0),  (1, 1)    # Bottom left, Bottom, Bottom right
    ]

    for col in range(start_col, end_col + 1):
        for dx, dy in adjacent_positions:
            new_row, new_col = start_row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols:
                char = matrix[new_row][new_col]
                if not (char.isalpha() or char.isdigit()) and char != '.':
                    isValid = True
                if char == '*':
                    potentialGear = (new_row, new_col)

    return isValid, potentialGear

# Process into a matrix
matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        matrix.append(list(line))

# Main logic
part1, part2 = 0, 0
potential_gears = {}

for i in range(len(matrix)):
    j = 0
    while j < len(matrix[i]):
        if matrix[i][j].isdigit():
            start_col = j
            while j < len(matrix[i]) and matrix[i][j].isdigit():
                j += 1
            end_col = j - 1

            isValid, potential_gear = check_number_and_find_gear(matrix, i, start_col, end_col)

            if isValid:
                number = int(''.join(matrix[i][start_col:end_col+1]))
                part1 += number

            if potential_gear:
                append_gear(potential_gear, number)

        else:
            j += 1

for value in potential_gears.values():
    if len(value) == 2:
        part2 += value[0] * value[1]

print(f"Part 1 answer is {part1}")
print(f"Part 2 answer is {part2}")
