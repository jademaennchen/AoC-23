#AoC day_09



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append([list(map(int, line.strip().split()))])
        f.close()
    return lines


#part_1
#part_2
def calc_sum_of_extrapolated_values(histories, prev):
    running_sum = 0
    for history in histories:
        while not all(value == 0 for value in history[-1]):
            history.append([x - y for x, y in zip(history[-1][1:], history[-1])])
        if prev: running_sum += sum([layer[0] if i % 2 == 0 else -layer[0] for i, layer in enumerate(history)])
        else: running_sum += sum([layer[-1] for layer in history])
    return running_sum


#main
if __name__ == '__main__':
    histories = input_from_file("day_09/input.txt")
    print(calc_sum_of_extrapolated_values(histories))
