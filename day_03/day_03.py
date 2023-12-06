#AoC day_03
import numpy as np



#input
def input_from_file(file):
    lines = np.array([['' for _ in range(840)] for _ in range(140)])
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            lines[:, i] = list(line.strip())
        f.close()
    return lines

def create_dict_of_part_pos(plan):
    dict, cur_part, idx = {}, [], 0
    for j in range(len(plan)):
        for i in range(len(plan)):
            if plan[i, j].isdigit():
                if not cur_part: cur_part = [idx, plan[i, j], [(i, j)]]
                else:
                    cur_part[1] += (plan[i, j])
                    cur_part[2].append((i, j))
            else:
                dict, cur_part, idx = update_dict(dict, cur_part, idx)
        dict, cur_part, idx = update_dict(dict, cur_part, idx)
    return dict

def update_dict(dict, part, idx):
    if not part: return dict, part, idx
    for pos in part[2]:
        dict[pos[0], pos[1]] = [part[0], part[1]]
    return dict, [], idx + 1
    

#part_1
def calc_sum_of_part_numbers(plan, dict):
    symbols, saved_ids = ['*', '/', '+', '-', '=', '#', '%', '$', '&', '@'], []
    symbols_pos = [(i, j) for j in range(len(plan)) for i in range(len(plan)) if plan[i, j] in symbols]
    for i, symbol in enumerate(symbols_pos):
        saved_ids = new_part_numbers(dict, symbol, saved_ids)
    return sum([int(id[1]) for id in saved_ids])

def new_part_numbers(dict, symbol, ids):
    for i in range(symbol[0] - 1, symbol[0] + 2):
        for j in range(symbol[1] - 1, symbol[1] + 2):
            if dict.get((i, j)):
                if dict[i, j][0] not in [id[0] for id in ids]: ids.append((dict[i, j][0], dict[i, j][1]))
    return ids


#part_2
def calc_sum_of_gear_ratios(plan, dict):
    gears_pos = [(i, j) for i in range(len(plan)) for j in range(len(plan)) if plan[i][j] == '*']
    running_sum = 0
    for gear in gears_pos:
        running_sum += calc_gear_ratio(dict, gear)
    return running_sum

def calc_gear_ratio(dict, gear):
    count, ids = 0, []
    for i in range(gear[0] - 1, gear[0] + 2):
        for j in range(gear[1] - 1, gear[1] + 2):
            if dict.get((i, j)):
                if dict[i, j][0] not in [id[0] for id in ids]:
                    count += 1
                    ids.append((dict[i, j][0], dict[i, j][1]))
    if count == 2: return int(ids[0][1]) * int(ids[1][1])
    return 0


#main
if __name__ == '__main__':
    plan = input_from_file("day_03/input.txt")
    dict = create_dict_of_part_pos(plan)
    print(calc_sum_of_part_numbers(plan, dict))
    print(calc_sum_of_gear_ratios(plan, dict))
