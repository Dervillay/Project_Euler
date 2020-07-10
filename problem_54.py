from collections import Counter

with open('poker.txt', 'r') as f:
    file_lines = f.read().splitlines()

hands = []
order_of_card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Read file and put each pair of hands into hands list
for line in file_lines:
    new_hands = line.split(' ')
    hands.append([new_hands[:5], new_hands[5:]])

# Returns number representing the hand's rank and either an integer or list
# to be used as a decider

# Hands are enumerated as follows:
#   0 - High card
#   1 - One pair
#   2 - Two pairs
#   3 - Three of a kind
#   4 - Straight
#   5 - Flush
#   6 - Full House
#   7 - Four of a kind
#   8 - Straight flush
#   9 - Royal flush
def classify_hand(hand):
    card_values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    suit_counts = Counter(suits)
    card_value_counts = Counter(card_values)

    straight = False

    # Check for straight
    indices = []
    for card_value in card_values:
        indices.append(order_of_card_values.index(card_value))

    if sorted(indices) == list(range(min(indices), max(indices)+1)):
        straight = True

    # Check for flush
    if 5 in suit_counts.values():

        # Check for royal flush
        if set(card_values) == {'T', 'J', 'Q', 'K', 'A'}:
            return 9, None

        # Check for straight flush
        elif straight:
            return 8, max(indices)

        # Check four of a kind
        if 4 in card_value_counts.values():
            return 7, max(indices, key=indices.count)

        # Check for full house
        elif 2 in card_value_counts.values() and 3 in card_value_counts.values():
            return 6, max(indices, key=indices.count)

        # Otherwise just return flush
        else:
            return 5, max(indices)

    # Check if straight
    elif straight:
        return 4, max(indices)

    # Check if three of a kind
    elif 3 in card_value_counts.values():
        return 3, max(indices, key=indices.count)

    # Check if two pairs
    elif list(card_value_counts.values()).count(2) == 2:
        return 2, indices

    # Check if one pair
    elif 2 in card_value_counts.values():
        return 1, indices

    # Otherwise, must be a high card
    return 0, max(indices)

# Takes two hands (represented by lists) and returns 1 or 2 to represent the winner
def winner(hand1, decider1, hand2, decider2):
    if hand1 > hand2:
        return 1

    elif hand1 < hand2:
        return 2

    # Determine winner in all cases except when hand ranks
    # are two pairs or a pair
    elif type(decider1) == int:
        if decider1 > decider2:
            return 1
        else:
            return 2

    # Determine winner when both hands are two pairs or a pair
    else:
        hand1_pair = max(decider1, key=decider1.count)
        hand2_pair = max(decider2, key=decider2.count)

        if hand1_pair != hand2_pair:
            return winner(hand1, hand1_pair, hand2, hand2_pair)

        decider1 = list(filter(lambda x: x != hand1_pair, decider1))
        decider2 = list(filter(lambda x: x != hand2_pair, decider2))

        # Determine winner when both hands contain a pair
        if hand1 == 1:
            return winner(hand1, max(decider1), hand2, max(decider2))

        # Determine winner when both hands contain two pairs
        else:
            next_hand1_pair = max(decider1, key=decider1.count)
            next_hand2_pair = max(decider2, key=decider2.count)

            if next_hand1_pair != next_hand2_pair:
                return winner(hand1, next_hand1_pair, hand2, next_hand2_pair)

            new_decider1 = list(filter(lambda x: x != hand1_pair, decider1))
            new_decider2 = list(filter(lambda x: x != hand2_pair, decider2))

            return winner(hand1, max(new_decider1), hand2, max(new_decider2))


player1_wins = 0

# Determine winner for each pair of hands and count number of player 1 wins
for hand_pair in hands:
    hand1_rank, hand1_decider = classify_hand(hand_pair[0])
    hand2_rank, hand2_decider = classify_hand(hand_pair[1])

    if winner(hand1_rank, hand1_decider, hand2_rank, hand2_decider) == 1:
        player1_wins += 1

print(player1_wins)
