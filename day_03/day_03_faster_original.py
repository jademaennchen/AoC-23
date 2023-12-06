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


#part_1
def calc_sum_of_part_numbers(plan):
    part_numbers, cur_number = [], False
    for j in range(len(plan)):
        for i in range(len(plan)):
            if plan[i][j].isdigit():
                if not cur_number: part_numbers.append([plan[i][j], [i, j]])
                else: part_numbers[-1][0] += (plan[i][j])
                cur_number = True
            else:
                if cur_number: part_numbers[-1].append([i - 1, j])
                cur_number = False
        if cur_number:
            part_numbers[-1].append([i - 1, j])
            cur_number = False

    running_sum = 0
    idx = 0
    for number in part_numbers:
        if is_part_number(plan, number):
            idx += 1
            running_sum += int(number[0])
    print(idx)
    return running_sum

def is_part_number(plan, number):
    symbols = ['*', '/', '+', '-', '=', '#', '%', '$', '&', '@']
    top_left_x, top_left_y, bottom_right_x, bottom_right_y = number[1][0] - 1, number[1][1] - 1, number[2][0] + 2, number[2][1] + 2
    if top_left_x < 0: top_left_x = 0
    if top_left_y < 0: top_left_y = 0
    for symbol in symbols:
        if(symbol in plan[top_left_x:bottom_right_x, top_left_y:bottom_right_y]): return True
    return False


#main
if __name__ == '__main__':
    plan = input_from_file("day_03/input.txt")
    print(calc_sum_of_part_numbers(plan))
