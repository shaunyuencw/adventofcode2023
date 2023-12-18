from collections import deque
import time

part1, part2 = 0, 0

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def update_bounds(bounds, x, y):
    bounds['min_x'] = min(bounds['min_x'], x)
    bounds['max_x'] = max(bounds['max_x'], x)
    bounds['min_y'] = min(bounds['min_y'], y)
    bounds['max_y'] = max(bounds['max_y'], y)

def flood_fill(lagoon):
    # Find the starting point for the fill
    start_x, start_y = None, None
    for y, row in enumerate(lagoon):
        if '#' in row:
            start_y = y
            start_x = row.index('#') + 1
            if start_x < len(row) and lagoon[start_y][start_x] == '.':
                break
    
    if start_x is None or start_y is None:
        return  # No starting point found, possibly no boundary
    
    # Perform an iterative flood fill from the starting point
    queue = deque([(start_x, start_y)])
    target = '.'
    fill = 'X'
    while queue:
        x, y = queue.popleft()
        # Check bounds and target match
        if 0 <= x < len(lagoon[0]) and 0 <= y < len(lagoon) and lagoon[y][x] == target:
            lagoon[y][x] = fill
            # Add adjacent cells to queue
            queue.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])


bounds = {'min_x': 0, 'max_x': 0, 'min_y': 0, 'max_y': 0}
instructions = []
x, y = 0, 0
with open('input.txt', 'r') as file:
    for line in file:
        dir, distance, color = line.strip().split(' ')
        # print(f"dir: {dir}, distance: {distance}, color: {color}")
        distance = int(distance)
        # Calculate bounds
        dx, dy = directions[dir]
        x = x + dx * distance
        y = y + dy * distance
        update_bounds(bounds, x, y)

        instructions.append((dir, distance, color))

start = time.perf_counter()
# Create lagoon based on bounds
rows = bounds['max_y'] - bounds['min_y'] + 1
cols = bounds['max_x'] - bounds['min_x'] + 1
print(f"Bounds: {bounds}")
print(f"Rows: {rows}, Cols: {cols}")

# Initialize lagoon with rows and columns correctly
lagoon = [['.' for _ in range(cols)] for _ in range(rows)]

# Offset the starting coordinates by the minimum bounds
start_x, start_y = -bounds['min_x'], -bounds['min_y']
current_x, current_y = start_x, start_y
lagoon[current_y][current_x] = '#'

print(f"Instructions: {len(instructions)}")
for (dir, distance, color) in instructions:
    for i in range(distance):
        dx, dy = directions[dir]
        current_x += dx
        current_y += dy
        if 0 <= current_x < cols and 0 <= current_y < rows:
            lagoon[current_y][current_x] = '#'
        else:
            print(f"Error at ({current_x}, {current_y})")
            break

flood_fill(lagoon)
part1 = sum(row.count('X') for row in lagoon) + sum(row.count('#') for row in lagoon)
end = time.perf_counter()
print(f"Part 1: {part1}, processed in {end - start:.2f} seconds")

# For visualization
with open('vis.txt', 'w') as file:
    for row in lagoon:
        line = ' '.join(map(str, row)) 
        file.write(line + '\n') 

# for line in lagoon:
#     print(''.join(line))
