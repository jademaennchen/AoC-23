#AoC day_07



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip().split())
        f.close()
    return lines


#part_1
def calc_total_winnings(hands):
    ranks = []
    for hand in hands:
        letters, counts = [], []
        for c in hand[0]:
            if c not in letters:
                counts.append(hand[0].count(c))
                letters.append(c)
        counts = sorted(counts, reverse = True)
        ranks.append(hand + [get_hand_type(counts)])
    dict = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    ranks = sorted(ranks, key=lambda x: (x[2], dict[x[0][0]], dict[x[0][1]], dict[x[0][2]], dict[x[0][3]], dict[x[0][4]]), reverse = True)
    return sum([int(rank[1]) * (i + 1) for i, rank in enumerate(ranks)])

def get_hand_type(counts):
    if counts[0] == 5: return 0
    if counts[0] == 4: return 1
    if counts == [3, 2]: return 2
    if counts[0] == 3: return 3
    if counts == [2, 2, 1]: return 4
    if counts[0] == 2: return 5
    return 6


#part_2
def calc_total_winnings_with_jokers(hands):
    ranks = []
    for hand in hands:
        letters, counts, jokers = [], [], 0
        for c in hand[0]:
            if c == 'J': jokers += 1
            elif c not in letters:
                counts.append(hand[0].count(c))
                letters.append(c)
        counts = sorted(counts,  reverse = True)
        if jokers == 5: counts.append(5)
        else: counts[0] += jokers
        ranks.append(hand + [get_hand_type(counts)])
    dict = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
    ranks = sorted(ranks, key=lambda x: (x[2], dict[x[0][0]], dict[x[0][1]], dict[x[0][2]], dict[x[0][3]], dict[x[0][4]]), reverse = True)
    return sum([int(rank[1]) * (i + 1) for i, rank in enumerate(ranks)])


#main
if __name__ == '__main__':
    hands = input_from_file("day_07/input.txt")
    print(calc_total_winnings(hands))
    print(calc_total_winnings_with_jokers(hands))
