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
def calc_total_area(movement, any_in_lagoon):
    v, saved_pos, pos= {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}, [(0, 0)], (0, 0)
    for action in movement:
        pos = (pos[0] + v[action[0]][0] * int(action[1]), pos[1] + v[action[0]][1] * int(action[1]))
        saved_pos.append(pos)
    max_r, max_l, max_d, max_u = max(position[1] for position in saved_pos), -min(position[1] for position in saved_pos), max(position[0] for position in saved_pos), -min(position[0] for position in saved_pos)
    lagoon = [['.' for _ in range(max_r + max_l + 1)] for _ in range(max_d + max_u + 1)]
    for i, position in enumerate(saved_pos[:-1]):
        y_is_pos, x_is_pos = 1 if saved_pos[i + 1][0] - position[0] > -1 else -1, 1 if saved_pos[i + 1][1] - position[1] > -1 else -1
        for y in range(position[0] + max_u, saved_pos[i + 1][0] + max_u + y_is_pos, y_is_pos):
            for x in range(position[1] + max_l, saved_pos[i + 1][1] + max_l + x_is_pos, x_is_pos):
                lagoon[y][x] = '#'
    in_lagoon, visited = [any_in_lagoon], []
    while in_lagoon:
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y, new_x = in_lagoon[0][0] + dy, in_lagoon[0][1] + dx
            if lagoon[new_y][new_x] == '.' and (new_y, new_x) not in visited and (new_y, new_x) not in in_lagoon: in_lagoon.append((new_y, new_x))
        visited.append(in_lagoon[0])
        in_lagoon = in_lagoon[1:]
    return len(visited) + ''.join(''.join(line) for line in lagoon).count('#')


#main
if __name__ == '__main__':
    positions = input_from_file("day_18/input.txt")
    print(calc_total_area(positions, (40, 8)))
