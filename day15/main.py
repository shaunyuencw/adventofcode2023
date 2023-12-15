def hash(string):
    hash_val = 0
    for char in string:
        hash_val = (hash_val + ord(char)) * 17 % 256
    return hash_val

part1, part2 = 0, 0
boxes = [{} for _ in range(256)]
label_mapping = {}

with open('input.txt', 'r') as file:
    puzzles = file.read().split(',')

for i, puzzle in enumerate(puzzles):
    # Part 1
    puzzle_hash = hash(puzzle)
    part1 += puzzle_hash

    # Part 2
    if '=' in puzzle:
        label, focal_length = puzzle.split('=')
        focal_length = int(focal_length)
        box_num = label_mapping.get(label, hash(label)) # Check if label already exists, if not get hash label
        boxes[box_num][label] = focal_length # Set/Replace label with focal length
        label_mapping[label] = box_num # Save mapping for future reference

    if '-' in puzzle:
        label = puzzle.replace('-', '')

        box_num = label_mapping.get(label, None)
        if box_num is not None: # Remove if label exists
            del boxes[box_num][label]
            del label_mapping[label]

for box_num, box in enumerate(boxes):
    if len(box) > 0: # Only process if box is not empty
        for slot, lens in enumerate(box.values()):
            part2 += (box_num+1) * (slot+1) * lens

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")