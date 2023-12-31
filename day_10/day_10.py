#AoC day_10
import numpy as np, math



#input
def input_from_file(file):
    lines = [np.array([['' for _ in range(140)] for _ in range(140)])]
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            lines[0][:, i] = list(line.strip())
            for j, c in enumerate(line):
                if c == 'S': lines.append((j, i))
        f.close()
    return lines
    

#part_1
def calc_steps_to_farthest_point(layout, start, loop):
    steps, prev, cur = 1, start, (start[0] + 1, start[1])
    loop.append(start)
    while layout[cur] != 'S':
        loop.append(cur)
        prev, cur = get_next_pos(layout, prev, cur)
        steps += 1
    return math.ceil(steps / 2)

def get_next_pos(layout, prev, cur):
    if layout[cur] == '|' and cur[1] - prev[1] > 0: return cur, (cur[0], cur[1] + 1)
    if layout[cur] == '|' and prev[1] - cur[1] > 0: return cur, (cur[0], cur[1] - 1)
    if layout[cur] == '-' and cur[0] - prev[0] > 0: return cur, (cur[0] + 1, cur[1])
    if layout[cur] == '-' and prev[0] - cur[0] > 0: return cur, (cur[0] - 1, cur[1])
    if layout[cur] == 'L' and cur[1] - prev[1] > 0: return cur, (cur[0] + 1, cur[1])
    if layout[cur] == 'L' and prev[0] - cur[0] > 0: return cur, (cur[0], cur[1] - 1)
    if layout[cur] == 'J' and cur[1] - prev[1] > 0: return cur, (cur[0] - 1, cur[1])
    if layout[cur] == 'J' and cur[0] - prev[0] > 0: return cur, (cur[0], cur[1] - 1)
    if layout[cur] == '7' and prev[1] - cur[1] > 0: return cur, (cur[0] - 1, cur[1])
    if layout[cur] == '7' and cur[0] - prev[0] > 0: return cur, (cur[0], cur[1] + 1)
    if layout[cur] == 'F' and prev[1] - cur[1] > 0: return cur, (cur[0] + 1, cur[1])
    if layout[cur] == 'F' and prev[0] - cur[0] > 0: return cur, (cur[0], cur[1] + 1)


#part_2
def calc_number_of_enclosed_tiles(layout, loop):
    pipe_tiles, running_sum = ('|', 'S', 'L', 'J', '7', 'F'), 0
    for y in range(len(layout)):
        pipe_walls = 0
        last_pipe_down = None
        for x in range(len(layout)):
            if (x, y) in loop and layout[x, y] in pipe_tiles:
                pipe_walls += 1
                if layout[x, y] == pipe_tiles[0]: last_pipe_down = None
                else:
                    if (layout[x, y] in pipe_tiles[1:4] and last_pipe_down == 1) or (layout[x, y] in pipe_tiles[4:] and last_pipe_down == 0): pipe_walls -= 1
                    last_pipe_down = None if last_pipe_down in (0, 1) else 0 if layout[x, y] in pipe_tiles[1:4] else 1
            elif (x, y) not in loop and pipe_walls % 2 == 1: running_sum += 1
    return running_sum


#main
if __name__ == '__main__':
    (layout, start) , loop = input_from_file("day_10/input.txt"), []
    print(calc_steps_to_farthest_point(layout, start, loop))
    print(calc_number_of_enclosed_tiles(layout, loop))
