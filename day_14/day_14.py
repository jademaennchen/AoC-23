#AoC day_14
import copy as c


#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(list(line.strip()))
        f.close()
    return lines
    

#part_1
def calc_total_load(platform):
    platform, running_sum = list(map(list, zip(*platform[::-1]))), 0
    for row in platform:
        row = ['#'] + row + ['#']
        rocks = [x for x, c in enumerate(row) if c == '#']
        for i, rock in enumerate(rocks[0:-1]):
            rolling_stones = row[rock:rocks[i + 1] + 1].count('O')
            running_sum += sum([len(row) - j - 2 for j in range(rock, rock + rolling_stones)])
    return running_sum


#part_2
def calc_total_load_with_cycles(platform):
    platform, running_sum = list(map(list, zip(*platform)))[::-1], 0
    loop_end, loop_start, dict = find_loop_length(platform)
    final_pos = (10**9 - loop_end[0]) % (loop_end[0] - loop_start[0])
    for value in dict.values():
        if value[0] == loop_start[0] + final_pos: platform = list(map(list, zip(*value[1][::-1])))
    for i, row in enumerate(platform):
        running_sum += ''.join(row).count('O') * (len(row) - i)
    return running_sum

def find_loop_length(platform):
    dict = {}
    for count in range(10**9):
        for _ in range(4):
            for i, row in enumerate(platform):
                row = ['#'] + row + ['#']
                rocks = [x for x, c in enumerate(row) if c == '#']
                for j, rock in enumerate(rocks[0:-1]):
                    rolling_stones = row[rock:rocks[j + 1] + 1].count('O')
                    platform[i][rock:rocks[j + 1] - 1] = ['O'] * rolling_stones + ['.'] * (rocks[j + 1] - rock - rolling_stones - 1)
            platform = list(map(list, zip(*platform[::-1])))
        if str(platform) in dict: return (count + 1, platform), dict[str(platform)], dict
        dict[str(platform)] = count + 1, c.deepcopy(platform)


#main
if __name__ == '__main__':
    platform = input_from_file("day_14/input.txt")
    print(calc_total_load(platform))
    print(calc_total_load_with_cycles(platform))
