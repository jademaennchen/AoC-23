#AoC day_12



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            lines.append(line.strip().split())
            lines[i][1] = list(map(int, lines[i][1].split(",")))
        f.close()
    return lines
    

#part_1
def calc_sum_of_combinations(springs):
    running_sum = 0
    for spring in springs:
        count = get_all_combinations_for_spring_with_dict_opt(spring, 0, 0, 0, {})
        running_sum += count[1]
    return running_sum

def get_all_combinations_for_spring_with_dict_opt(spring, i, start, saved_marks, dict):
    combinations = 0
    if dict.get((i, start, saved_marks)) != None: return (dict, dict[i, start, saved_marks])
    for j in range(start, len(spring[0]) - 1 - (sum(spring[1][i:]) - 1 + len(spring[1]) - i - 2)):
        added_marks = saved_marks
        if all(spring[0][k] in ('?', '#') for k in range(j, j + spring[1][i])):
            for l in range(j, j + spring[1][i]):
                if spring[0][l] == '?': added_marks += 1
            if i == len(spring[1]) - 1: combinations += 1 if spring[0].count('#') + added_marks == sum(spring[1]) else 0
            elif spring[0][j + spring[1][i]] != '#':
                result = get_all_combinations_for_spring_with_dict_opt(spring, i + 1, j + spring[1][i] + 1, added_marks, dict)
                dict, combinations = result[0], combinations + result[1]
    dict[i, start, saved_marks] = combinations
    return (dict, combinations)


#part_2
def calc_sum_of_combinations_with_unfolded_input(springs):
    running_sum = 0
    for spring in springs:
        spring[0] = '?'.join([spring[0]] * 5)
        spring[1] *= 5
        count = get_all_combinations_for_spring_with_dict_opt(spring, 0, 0, 0, {})
        running_sum += count[1]
    return running_sum


#main
if __name__ == '__main__':
    springs = input_from_file("day_12/input.txt")
    print(calc_sum_of_combinations(springs))
    print(calc_sum_of_combinations_with_unfolded_input(springs))
