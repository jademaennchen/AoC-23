#AoC day_05



#input
def input_from_file(file):
    lines, j = [[],[]], -1
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            if i == 0: lines[0] += (list(map(int, line[7:].strip().split())))
            elif len(line) == 1:
                lines[1].append([])
                j += 1
            elif line[0].isdigit(): lines[1][j] += [list(map(int, line.strip().split()))]
        f.close()
    return lines


#part_1
def calc_lowest_location_value(seeds, almanac):
    min_location = float('inf')
    for seed in seeds:
        for conversion in almanac:
            for conversion_range in conversion:
                if seed < conversion_range[1] + conversion_range[2] and seed >= conversion_range[1]:
                    seed = conversion_range[0] + seed - conversion_range[1]
                    break
        if seed < min_location: min_location = seed
    return min_location


#part_2
def calc_lowest_locaction_value_with_location_ranges(seeds, almanac):
    seeds, new_seeds = [[x, x + y - 1] for x, y in zip(seeds[::2], seeds[1::2])], []
    for conversions in almanac:
        for seed_range in seeds:
            for conv_range in conversions:
                if seed_range[0] >= conv_range[1] + conv_range[2] or seed_range[1] < conv_range[1]: continue
                elif seed_range[0] >= conv_range[1] and seed_range[1] < conv_range[1] + conv_range[2]:
                    new_seeds.append([conv_range[0] + seed_range[0] - conv_range[1], conv_range[0] + seed_range[1] - conv_range[1]])
                    seed_range = []
                    break
                elif seed_range[0] >= conv_range[1] and seed_range[1] >= conv_range[1] + conv_range[2]:
                    new_seeds.append([conv_range[0] + seed_range[0] - conv_range[1], conv_range[0] + conv_range[2] - 1])
                    seed_range = [conv_range[1] + conv_range[2], seed_range[1]]
                elif seed_range[0] < conv_range[1] and seed_range[1] < conv_range[1] + conv_range[2]:
                    new_seeds.append([conv_range[0], conv_range[0] + seed_range[1] - conv_range[1]])
                    seed_range = [seed_range[0], conv_range[1] - 1]
            if seed_range: new_seeds.append(seed_range)
        seeds, new_seeds = new_seeds, []
    return min([seed[0] for seed in seeds])


#main
if __name__ == '__main__':
    seeds, almanac = input_from_file("day_05/input.txt")
    print(calc_lowest_location_value(seeds, almanac))
    print(calc_lowest_locaction_value_with_location_ranges(seeds, almanac))
