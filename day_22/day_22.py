#AoC day_22



#input
def input_from_file(file):
    lines = [[[['.' for _ in range(10)] for _ in range(10)]] + [[[':' for _ in range(10)] for _ in range(10)] for _ in range(400)], {}]
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            s, e = [list(map(int, j.split(','))) for j in line.strip().split('~')]
            lines[1][str(i)] = [False, [], [], []]
            for z, y, x in [(z, y, x) for x in range(s[0], e[0]+1) for y in range(s[1], e[1]+1) for z in range(s[2], e[2]+1)]:
                lines[0][z][y][x] = str(i)
                lines[1][str(i)][1].append([z, y, x])
        f.close()
    return lines


#part_1
#part_2
def calc_disintegrable_bricks(snapshot, bricks, part2):
    running_sum = 0
    for z, y, x in [(z, y, x) for z in range(1, len(snapshot)) for y in range(len(snapshot[0])) for x in range(len(snapshot[0][0]))]:
        c = snapshot[z][y][x]
        if c in bricks and bricks[c][0] == False:
            positions, bricks[c][0], dif = bricks[c][1], True, 0
            while all(snapshot[b_z-1][b_y][b_x] in (c, ':') for b_z, b_y, b_x in positions):
                dif += 1
                for pos in positions: pos[0] -= 1
            for b_z, b_y, b_x in positions:
                snapshot[b_z+dif][b_y][b_x], snapshot[b_z][b_y][b_x], sub_c  = ':', c, snapshot[b_z-1][b_y][b_x]
                if sub_c not in (':', '.', c) and c not in bricks[sub_c][2]:
                    bricks[sub_c][2].append(c)
                    bricks[c][3].append(sub_c)
    if not part2: return sum([1 for brick in bricks.keys() if all(len(bricks[sup_bricks][3]) > 1 for sup_bricks in bricks[brick][2])])
    for brick in bricks.keys():
        cur_layer, old_len = [new_brick for new_brick in bricks[brick][2] if len(bricks[new_brick][3]) == 1], 0
        while len(cur_layer) > old_len:
            old_len = len(cur_layer)
            for sup_brick in cur_layer:
                cur_layer.extend([new_brick for new_brick in bricks[sup_brick][2] if all(cur_bricks in cur_layer for cur_bricks in bricks[new_brick][3]) and new_brick not in cur_layer])
        running_sum += old_len
    return running_sum


#main
if __name__ == '__main__':
    snapshot, bricks = input_from_file("day_22/input.txt")
    print(calc_disintegrable_bricks(snapshot, bricks, False))
    print(calc_disintegrable_bricks(snapshot, bricks, True))
