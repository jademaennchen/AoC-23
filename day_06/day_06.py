#AoC day_06



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip().split()[1:])
        f.close()
    return lines


#part_1
def calc_total_winning_combinations(race_data):
    race_data, running_product = [[int(x), int(y)] for x, y in zip(race_data[0], race_data[1])], 1
    for race in race_data:
        for i in range(1, race[0] // 2 + 1):
            if i * (race[0] - i) >= race[1]:
                running_product *= race[0] - (i - 1) * 2 - 1
                break
    return running_product


#part_2
def calc_total_winning_combinations_for_singular_race(race_data):
    race = [int("".join(race_data[0])), int("".join(race_data[1]))]
    for i in range(1, race[0] // 2 + 1):
        if i * (race[0] - i) >= race[1]:
            return race[0] - (i - 1) * 2 - 1


#main
if __name__ == '__main__':
    race_data = input_from_file("day_06/input.txt")
    print(calc_total_winning_combinations(race_data))
    print(calc_total_winning_combinations_for_singular_race(race_data))
