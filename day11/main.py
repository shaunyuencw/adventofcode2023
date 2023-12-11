import math
import itertools

def get_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]) # Manhatten distance

def is_empty_galaxy(star_list):
    return all(star == '.' for star in star_list)

def dp_count_spaces(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp_matrix = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
    empty_rows, empty_cols = 0, 0

    # Counting empty rows
    for row in range(rows):
        if is_empty_galaxy(matrix[row]):
            empty_rows += 1
        for col in range(cols):
            dp_matrix[row][col] = (empty_rows, dp_matrix[row][col][1])

    # Counting empty columns
    for col in range(cols):
        # Extracting column view
        column_view = [matrix[row][col] for row in range(rows)]
        if is_empty_galaxy(column_view):
            empty_cols += 1
        for row in range(rows):
            dp_matrix[row][col] = (dp_matrix[row][col][0], empty_cols)

    return dp_matrix

def get_expanded_coord(dp_empcount_matrix, galaxy_coord, age = 1):
    empty_rows, empty_cols = dp_empcount_matrix[galaxy_coord[0]][galaxy_coord[1]]

    return (galaxy_coord[0] + empty_rows * age, galaxy_coord[1] + empty_cols * age)

# Process into a matrix
universe = []
galaxies = {}

line_id, galaxy_id = 0, 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        universe_line = list(line)
        for id, char in enumerate(universe_line):
            if char == "#":
                galaxies[galaxy_id] = (line_id, id)
                galaxy_id += 1
    
        universe.append(universe_line)
        line_id += 1

dp_empcount_matrix = dp_count_spaces(universe)
part1, part2 = 0, 0

combinations = itertools.combinations(galaxies.keys(), 2) # All pair combinations
for g1, g2 in combinations:
    g1_expanded = get_expanded_coord(dp_empcount_matrix, galaxies[g1])
    g2_expanded = get_expanded_coord(dp_empcount_matrix, galaxies[g2])

    aged_g1 = get_expanded_coord(dp_empcount_matrix, galaxies[g1], age = 999999)
    aged_g2 = get_expanded_coord(dp_empcount_matrix, galaxies[g2], age = 999999)

    distance = get_distance(g1_expanded, g2_expanded)
    aged_distance = get_distance(aged_g1, aged_g2)

    part1 += distance
    part2 += aged_distance

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")