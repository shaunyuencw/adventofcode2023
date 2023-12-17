import time
import heapq
import functools
with open('input.txt', 'r') as file:
    matrix = [list(map(int, line.strip())) for line in file]

def find_min_heat_loss(matrix, is_part2=False):
    rows, cols = len(matrix), len(matrix[0])
    directions = ['N', 'E', 'S', 'W']  # North, East, South, West
    direction_deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    def get_neighbors(x, y, dir_index, steps, part1=False):
        neighbors = []
        dx, dy = direction_deltas[dir_index]

        if not is_part2: # Part 1
            # Straight move
            if steps < 3:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    neighbors.append((nx, ny, dir_index, steps + 1))
            
            # Left and right turns
            left = (dir_index - 1) % 4
            right = (dir_index + 1) % 4
            for turn in [left, right]:
                ndx, ndy = direction_deltas[turn]
                nx, ny = x + ndx, y + ndy
                if 0 <= nx < cols and 0 <= ny < rows:
                    neighbors.append((nx, ny, turn, 1))
        else: # Part 2
            # Straight move (minimum 4 steps, maximum 10 steps)
            if steps < 10:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    neighbors.append((nx, ny, dir_index, steps + 1))

            # Allow turning after at least 4 steps
            if steps >= 4:
                left = (dir_index - 1) % 4
                right = (dir_index + 1) % 4
                for turn in [left, right]:
                    ndx, ndy = direction_deltas[turn]
                    nx, ny = x + ndx, y + ndy
                    if 0 <= nx < cols and 0 <= ny < rows:
                        neighbors.append((nx, ny, turn, 1))

        return neighbors

    @functools.lru_cache(maxsize=None)
    def heuristic(x, y):
        # Euclidean distance to the bottom right corner
        return ((cols - x) ** 2 + (rows - y) ** 2) ** 0.5

    # Priority queue: (estimated_total_heat_loss, actual_heat_loss, x, y, direction index, steps, path)
    pq = [(heuristic(0, 0), 0, 0, 0, 1, 0, [(0, 0)])]  # Start path from (0, 0)

    visited = set()

    while pq:
        estimated_total, heat_loss, x, y, dir_index, steps, path = heapq.heappop(pq)

        if (x, y) == (cols - 1, rows - 1): # Ending must be at least 4 steps away
            if is_part2:
                if steps >= 4:
                    return heat_loss, path
            else:
                return heat_loss, path

        if (x, y, dir_index, steps) in visited:
            continue

        visited.add((x, y, dir_index, steps))

        for nx, ny, nd, nsteps in get_neighbors(x, y, dir_index, steps):
            new_heat_loss = heat_loss + int(matrix[ny][nx])
            new_path = path + [(nx, ny)]
            estimated_total = new_heat_loss + heuristic(nx, ny)
            heapq.heappush(pq, (estimated_total, new_heat_loss, nx, ny, nd, nsteps, new_path))

    return float('inf'), []  # If no path is found

def visualize_path(matrix, path):
    path_visual = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, y in path:
        path_visual[y][x] = matrix[y][x]
    
    for row in path_visual:
        print("".join(map(str, row)))

start = time.perf_counter()
part1, path1 = find_min_heat_loss(matrix)
end = time.perf_counter()
# visualize_path(matrix, path1)
print(f"Part 1: {part1}, processed in {end - start:.2f} seconds")

start = time.perf_counter()
part2, path2 = find_min_heat_loss(matrix, is_part2=True)
end = time.perf_counter()
# visualize_path(matrix, path2)
print(f"Part 2: {part2}, processed in {end - start:.2f} seconds")