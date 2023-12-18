import time

def hex_to_instruction(color):
    color = color.replace('(', '').replace(')', '').replace('#', '')
    distance = int(color[:5], 16) # Distance is the first 5 digits in hexa
    instruction = color[-1] # Last character is the instruction
    # print(f"distance: {distance}, instruction: {instruction}")

    return distance, instruction

def calculate_perimeter(coords):
    """Calculate the perimeter of a polygon given its coordinates."""
    perimeter = 0
    for i in range(len(coords)):
        x0, y0 = coords[i]
        x1, y1 = coords[(i + 1) % len(coords)]
        perimeter += ((x1 - x0)**2 + (y1 - y0)**2)**0.5
    return perimeter

def shoelace_area(coordinates):
    n = len(coordinates)
    sum1 = 0
    sum2 = 0

    for i in range(n):
        x_i, y_i = coordinates[i]
        # Get the next vertex (wrapping around to the first vertex at the end)
        x_next, y_next = coordinates[(i + 1) % n]
        sum1 += x_i * y_next
        sum2 += y_i * x_next

    # The area is half the absolute value of the difference between the two sums
    area = abs(sum1 - sum2) / 2
    return area

x, y, x2, y2 = 0, 0, 0, 0
points_part1 = [(x, y)]
points_part2 = [(x, y)]


part1, part2 = 0, 0

instructions = {
    '3': (-1, 0),
    '1': (1, 0),
    '2': (0, -1),
    '0': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

with open('input.txt', 'r') as file:
    for line in file:
        instruction, distance, color = line.strip().split(' ')
        distance = int(distance)
        # Part 1
        dx, dy = instructions[instruction]

        x = x + dx * distance
        y = y + dy * distance

        points_part1.append((x, y))

        # Part2
        distance, instruction = hex_to_instruction(color)
        dx, dy = instructions[instruction]
        
        x2 = x2 + dx * distance
        y2 = y2 + dy * distance

        points_part2.append((x2, y2))

start1 = time.perf_counter()
part1 = int(shoelace_area(points_part1) + calculate_perimeter(points_part1) // 2 + 1)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2 = int(shoelace_area(points_part2) + calculate_perimeter(points_part2) // 2 + 1)
end2 = time.perf_counter()

print(f"Part 1: {part1}, processed in {end1 - start1:.2f} seconds")
print(f"Part 2: {part2}, processed in {end2 - start2:.2f} seconds")