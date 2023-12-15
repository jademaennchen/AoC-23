#AoC day_15



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines += list(line.strip().split(","))
        f.close()
    return lines
    

#part_1
def calc_sum_of_parsed_steps(orders):
    running_sum = 0
    for order in orders:
        running_sum += hash_algorithm(order)
    return running_sum

def hash_algorithm(code):
    ret = ord(code[0]) * 17 % 256
    for c in code[1:]:
        ret = (ret + ord(c)) * 17 % 256
    return ret


#part_2
def calc_focusing_power(steps):
    boxes = [[] for _ in range(256)]
    for step in steps:
        box_index = hash_algorithm(''.join(c for c in step if c.isalpha()))
        if '-' in step:
            for lens in boxes[box_index]:
                if lens[0] == step[:-1]: boxes[box_index].remove(lens)
        else:
            for lens in boxes[box_index]:
                if lens[0] == step[:-2]:
                    lens[1] = step[-1]
                    break
            else: boxes[box_index].append([step[:-2], step[-1]])
    return sum((i + 1) * (j + 1) * int(lens[1]) for i, box in enumerate(boxes) for j, lens in enumerate(box))


#main
if __name__ == '__main__':
    orders = input_from_file("day_15/input.txt")
    print(calc_sum_of_parsed_steps(orders))
    print(calc_focusing_power(orders))
