from collections import Counter

def card_value(card):
    order = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return order[card]

def hand_sort_key(hand_bid_tuple):
    hand, bid = hand_bid_tuple
    return ([card_value(card) for card in hand], bid)

def classify_hand(hand_count):
    most_common = hand_count.most_common(2)
    counts = [count for card, count in most_common]

    if counts[0] == 2:
        return '2 Pair' if counts[1] == 2 else '1 Pair'
    elif counts[0] == 3:
        return 'Full House' if counts[1] == 2 else '3 of a kind'
    elif counts[0] == 4:
        return '4 of a kind'
    elif counts[0] == 5:
        return '5 of a kind'
    else:
        return 'Nothing'

hand_strength = {key: [] for key in ['Nothing', '1 Pair', '2 Pair', '3 of a kind', 'Full House', '4 of a kind', '5 of a kind']}
with open('input.txt', 'r') as file:
    for line in file:
        hand, bid = line.strip().split(' ')
        bid = int(bid)

        hand_count = Counter(hand)
        category = classify_hand(hand_count)
        
        hand_strength[category].append((hand, bid))

# Calculate score
part1, rank = 0, 1
for category in ['Nothing', '1 Pair', '2 Pair', '3 of a kind', 'Full House', '4 of a kind', '5 of a kind']:
    for hand, bid in sorted(hand_strength[category], key=hand_sort_key):
        part1 += bid * rank
        rank += 1

print(f"Part 1: {part1}")