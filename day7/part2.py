from collections import Counter

def card_value(card):
    order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    return order.get(card, 0)  # Jacks are worth 0 now

def hand_sort_key(hand_bid_tuple):
    hand, bid = hand_bid_tuple
    return ([card_value(card) for card in hand], bid)

def convert_jacks(hand):
    non_j_cards = [card for card in hand if card != 'J']
    count = Counter(non_j_cards)
    
    if non_j_cards:
        most_common = count.most_common(1)[0]
        highest_count = most_common[1]

        is_tie = sum(cnt == highest_count for card, cnt in count.items()) > 1

        if is_tie:
            conversion = max(non_j_cards, key=card_value)
        else:
            conversion = most_common[0]
    else:
        conversion = 'A'

    return ''.join(conversion if card == 'J' else card for card in hand)


def classify_hand(hand_count):
    most_common = hand_count.most_common(2)
    counts = [count for card, count in most_common]

    if counts[0] == 2:
        return '2 Pair' if len(counts) > 1 and counts[1] == 2 else '1 Pair'
    elif counts[0] == 3:
        return 'Full House' if len(counts) > 1 and counts[1] == 2 else '3 of a kind'
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

        joker_hand = convert_jacks(hand)
        hand_count = Counter(joker_hand)
        category = classify_hand(hand_count)
        
        hand_strength[category].append((hand, bid))
        
# Calculate score
part2, rank = 0, 1
for category in ['Nothing', '1 Pair', '2 Pair', '3 of a kind', 'Full House', '4 of a kind', '5 of a kind']:
    for hand, bid in sorted(hand_strength[category], key=hand_sort_key):
        part2 += bid * rank
        rank += 1

print(f"Part 2: {part2}")
