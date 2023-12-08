import math

def lcm_of_list(numbers):
    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = current_lcm * number // math.gcd(current_lcm, number)
    return current_lcm

def parse_value(value_str):
    value_str = value_str[1:-1].strip()  # Remove parentheses
    value_parts = value_str.split(",")
    return tuple(v.strip() for v in value_parts) if len(value_parts) == 2 else None

def process_file(file_path):
    mapping = {}
    instruction_set = ""
    starting_positions = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if not instruction_set:
                instruction_set = line
            else:
                key, value_str = (part.strip() for part in line.split("=", 1))
                value = parse_value(value_str)
                if value:
                    mapping[key] = value
                    if key[2] == 'A':
                        starting_positions[key] = 0

    return instruction_set, mapping, starting_positions

def is_end_position(position, is_part1):
    return position == "ZZZ" if is_part1 else position[2] == "Z"

def find_moves_needed(instruction_set, mapping, starting_position, is_part1):
    position = starting_position
    moves = 0

    while not is_end_position(position, is_part1):
        instruction = instruction_set[moves % len(instruction_set)]
        position = mapping[position][0 if instruction == 'L' else 1]
        moves += 1

    return moves


instruction_set, mapping, starting_positions = process_file('input.txt')

# For part 1
part1 = find_moves_needed(instruction_set, mapping, "AAA", True)

# For part 2
starting_positions_part2 = {k: 0 for k in mapping if k[2] == 'A'}
moves_needed_part2 = [find_moves_needed(instruction_set, mapping, pos, False) for pos in starting_positions_part2]
part2 = lcm_of_list(moves_needed_part2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")