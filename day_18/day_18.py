#AoC day_18



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip().split())
        f.close()
    return lines
    

#part_1
def calc_total_area(movement):
    movement, vecs, saved_pos, pos, running_sum = [movement[-1]] + movement + [movement[0]], {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}, [(0, 0)], (0, 0), 0
    outer_corner, inner_corner = [('U', 'R', 'D'), ('R', 'D', 'L'), ('D', 'L', 'U'), ('L', 'U', 'R')], [('D', 'R', 'U'), ('R', 'U', 'L'), ('U', 'L', 'D'), ('L', 'D', 'R')]
    for i, action in enumerate(movement[1:-1], 1):
        adjust = 1 if (movement[i - 1][0], action[0], movement[i + 1][0]) in outer_corner else -1 if (movement[i - 1][0], action[0], movement[i + 1][0]) in inner_corner else 0
        pos = (pos[0] + vecs[action[0]][0] * (int(action[1]) + adjust), pos[1] + vecs[action[0]][1] * (int(action[1]) + adjust))
        saved_pos.append(pos)
    for point_1, point_2 in zip(saved_pos[:-1], saved_pos[1:]):
        running_sum += point_1[1] * point_2[0] - point_1[0] * point_2[1]
    return int(running_sum / 2)


#part_2
def calc_total_area_from_hex(movement):
    vecs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    for i, action in enumerate(movement):
        movement[i] = [vecs[action[2][7]], int(action[2][2:-2], 16)]
    return calc_total_area(movement)


#main
if __name__ == '__main__':
    positions = input_from_file("day_18/input.txt")
    print(calc_total_area(positions))
    print(calc_total_area_from_hex(positions))
