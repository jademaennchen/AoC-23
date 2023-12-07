#AoC day_04



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines += [[j.split() for j in line.strip().replace(":", "|").split("|")[1:]]]
        f.close()
    return lines


#part_1
def calc_total_points(cards):
    running_sum = 0
    for card in cards:
        wins = sum(1 for number in card[1] if number in card[0])
        if wins > 0: running_sum += pow(2, wins - 1)
    return running_sum


#part_2
def calc_total_cards(cards):
    count = [1 for _ in range(len(cards))]
    for i, card in enumerate(cards):
        wins = sum(1 for number in card[1] if number in card[0])
        for j in range(i + 1, i + wins + 1):
            count[j] += count[i] * 1
    return sum(count)


#main
if __name__ == '__main__':
    cards = input_from_file("day_04/input.txt")
    print(calc_total_points(cards))
    print(calc_total_cards(cards))
