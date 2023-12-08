#AoC day_08
import math



#input
def input_from_file(file):
    lines = [[]]
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            if i == 0: lines += line.strip().split()
            elif i > 1: lines[0].append((line[0:3], line[7:10], line[12:15]))
        f.close()
    return lines


#part_1
def calc_number_of_steps(vertices, order):
    dict, current, i = {}, 'AAA', 0
    for vertex in vertices:
        dict[vertex[0]] = (vertex[1], vertex[2])
    while True:
        if current == 'ZZZ': return i
        if order[i % len(order)] == 'L': current = dict[current][0]
        else: current = dict[current][1]
        i += 1


#part_2
def calc_number_of_steps_with_all_a_starts(vertices, order):
    dict, currents, i = {}, [], 0
    for vertex in vertices:
        dict[vertex[0]] = (vertex[1], vertex[2])
        if vertex[0][2] == 'A': currents.append([vertex[0], None])
    while True:
        if all(type(current[1]) == int for current in currents): break
        sign = 0 if order[i % len(order)] == 'L' else 1
        for j, current in enumerate(currents):
            if current[0][2] == 'Z': currents[j][1] = i
            currents[j][0] = dict[current[0]][sign]
        i += 1
    return math.lcm(*[current[1] for current in currents])


#main
if __name__ == '__main__':
    vertices, order = input_from_file("day_08/input.txt")
    print(calc_number_of_steps(vertices, order))
    print(calc_number_of_steps_with_all_a_starts(vertices, order))
