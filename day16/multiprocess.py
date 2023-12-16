from multiprocessing import Pool, Manager
import time

def is_valid_point(x, y, width, height):
    return 0 <= x < height and 0 <= y < width

def count_powered_cells(powered_cells):
    return sum(sum(row) for row in powered_cells)

def process_start_point(start_point, matrix, directions, left_mirror, right_mirror):
    return count_powered_cells(process_points([start_point], matrix, directions, left_mirror, right_mirror))

def process_points(points, matrix, directions, left_mirror, right_mirror):
    checked = set()
    powered_cells = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    
    while points:
        x, y, direction = points.pop(0)
        if (x, y, direction) in checked or not is_valid_point(x, y, len(matrix[0]), len(matrix)):
            continue

        checked.add((x, y, direction))
        powered_cells[x][y] = True
        square = matrix[x][y]

        if square == '.':
            next_x, next_y = x + directions[direction][0], y + directions[direction][1]
            points.append((next_x, next_y, direction))
        elif square in ['|', '-']:
            for dir in ['N', 'S'] if square == '|' else ['E', 'W']:
                next_x, next_y = x + directions[dir][0], y + directions[dir][1]
                points.append((next_x, next_y, dir))
        elif square in ['\\', '/']:
            new_direction = right_mirror[direction] if square == '\\' else left_mirror[direction]
            next_x, next_y = x + directions[new_direction][0], y + directions[new_direction][1]
            points.append((next_x, next_y, new_direction))

    return powered_cells

def main():
    global shared_matrix
    manager = Manager()

    # Read matrix and initialize variables
    with open('input.txt', 'r') as file:
        matrix = file.read().splitlines()

    shared_matrix = manager.list(matrix)

    directions = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
    left_mirror = {'E': 'N', 'S': 'W', 'W': 'S', 'N': 'E'}
    right_mirror = {'E': 'S', 'S': 'E', 'W': 'N', 'N': 'W'}

    width, height = len(matrix[0]), len(matrix)
    points = [(0, 0, 'E')]
    powered_cells = process_points(points, matrix, directions, left_mirror, right_mirror)
    part1 = count_powered_cells(powered_cells)
    print(f"Part 1: {part1}")

    start_time = time.perf_counter()
    # Part 2 with multiprocessing
    all_start_points = [(0, y, 'S') for y in range(width)] + \
                        [(height - 1, y, 'N') for y in range(width)] + \
                        [(x, 0, 'E') for x in range(height)] + \
                        [(x, width - 1, 'W') for x in range(height)]
    
    # Prepare data to be passed to process_start_point
    data = [(sp, matrix, directions, left_mirror, right_mirror) for sp in all_start_points]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.starmap(process_start_point, data)

    part2 = max(results)
    end_time = time.perf_counter()
    print(f"Part 2: {part2}, processed in {end_time - start_time:0.2f} seconds")

if __name__ == '__main__':
    main()