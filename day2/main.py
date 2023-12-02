inventory = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

ans = 0
part2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        # Split the line at the colon
        split_line = line.split(':')

        # Extract and convert the game ID
        game_id = int(split_line[0].strip().split(' ')[1])

        game_valid = True

        # Get the rest of the string after the colon
        game_data = split_line[1].strip()

        # Split the game data into a list of words
        rounds = [data.strip() for data in game_data.split(';')]

        round_num = 1
        max_needed = {"red": 0, "green": 0, "blue": 0}


        print(f"Game {game_id}")
        for round in rounds:
            # Split the round into a list of words
            draws = [data.strip() for data in round.split(',')]

            print(f"Round {round_num}: {draws}")

            for draw in draws:
                num_cube = int(draw.split(' ')[0])
                color = draw.split(' ')[1]

                # Part 1
                if color in inventory.keys():
                    if inventory[color] < num_cube:
                        game_valid = False

                # Part 2
                if color in max_needed.keys():
                    if num_cube > max_needed[color] :
                        max_needed[color] = num_cube

            round_num += 1

        temp = 1
        for val in max_needed.values():
            temp *= val
        
        print(f"Max needed: {max_needed}")
        print(f"Product: {temp}")

        part2 += temp 

        if game_valid:
            ans += game_id

print(f"Part 1: {ans}")
print(f"Part 2: {part2}")