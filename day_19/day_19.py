#AoC day_19
import math, copy


#input
def input_from_file(file):
    lines = [[], {}]
    with open(file) as f:
        for line in f.readlines():
            if line[0] == '{': lines[0].append([int(j[2:]) for j in line.strip()[1:-1].split(',')])
            elif len(line) > 1: lines[1][line.split('{')[0]] = [j.split(':') for j in line.strip()[:-1].split('{')[1].split(',')]
        f.close()
    return lines


#part_1
def calc_sum_of_accepted_part_ratings(parts, workflows):
    running_sum = 0
    for part in parts[0:]:
        cur_key = 'in'
        while True:
            cur_key = get_next_key_from_workflow(workflows[cur_key], part)     
            if cur_key == 'A': running_sum += sum(part)
            if cur_key == 'A' or cur_key == 'R': break
    return running_sum

def get_next_key_from_workflow(workflow, part):
    qualities = {'x': 0, 'm': 1, 'a': 2, 's': 3}
    for rule in workflow[:-1]:
        if rule[0][1] == '<' and part[qualities[rule[0][0]]] < int(rule[0][2:]): return rule[1]
        elif rule[0][1] == '>' and part[qualities[rule[0][0]]] > int(rule[0][2:]): return rule[1]
    return workflow[-1][0]


#part_2
def calc_total_accepted_part_ratings(workflows):
    part_ranges, count = [[[1, 1, 1, 1], [4000, 4000, 4000, 4000], 'in']], 0
    while part_ranges:
        part_range = part_ranges[0]
        if part_range[2] == 'A': count += math.prod([part_range[1][i] - part_range[0][i] + 1 for i in range(4)])
        elif part_range[2] != 'R': part_ranges.extend(get_new_ranges_from_workflow(workflows[part_range[2]], part_range))
        part_ranges = part_ranges[1:]
    return count

def get_new_ranges_from_workflow(workflow, part_range):
    qualities, new_ranges = {'x': 0, 'm': 1, 'a': 2, 's': 3}, []
    for rule in workflow[:-1]:
        sign_index = qualities[rule[0][0]]
        if rule[0][1] == '<' and part_range[1][sign_index] < int(rule[0][2:]): return new_ranges.append([part_range[0], part_range[1], rule[1]])
        elif rule[0][1] == '>' and part_range[0][sign_index] > int(rule[0][2:]): return new_ranges.append([part_range[0], part_range[1], rule[1]])
        elif rule[0][1] == '<' and part_range[0][sign_index] < int(rule[0][2:]):
            new_ranges.append(copy.deepcopy(part_range))
            new_ranges[-1][1][sign_index], new_ranges[-1][2], part_range[0][sign_index] = int(rule[0][2:]) - 1, rule[1], int(rule[0][2:])
        elif rule[0][1] == '>' and part_range[1][sign_index] > int(rule[0][2:]):
            new_ranges.append(copy.deepcopy(part_range))
            new_ranges[-1][0][sign_index], new_ranges[-1][2], part_range[1][sign_index] = int(rule[0][2:]) + 1, rule[1], int(rule[0][2:])
    new_ranges.append([part_range[0], part_range[1], workflow[-1][0]])
    return new_ranges


#main
if __name__ == '__main__':
    parts, workflows = input_from_file("day_19/input.txt")
    print(calc_sum_of_accepted_part_ratings(parts, workflows))
    print(calc_total_accepted_part_ratings(workflows))
