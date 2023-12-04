part1 = 0
card_num = 1

my_nums = []
winning_nums = []
card_instances = {}

with open('input.txt', 'r') as file:
    for line in file:
        # Split the line and strip only the relevant part
        line = line.split(':')[1].strip()
        # Use set comprehension directly
        my_nums, winning_nums = (set(int(num) for num in part.split()) for part in line.split('|'))

        card_instances[card_num] = card_instances.get(card_num, 0) + 1 # My original copy

        # Find intersection
        my_wins = my_nums.intersection(winning_nums)
        
        if my_wins:
            part1 += 2**(len(my_wins) - 1)

        current_card_instances = card_instances.get(card_num, 0)
        for sub_card in range(1, len(my_wins) + 1):
            card_instances[card_num + sub_card] = card_instances.get(card_num + sub_card, 0) + current_card_instances

        card_num += 1

print(f"Part 1: {part1}")
print(f"Part 2: {sum(card_instances.values())}")