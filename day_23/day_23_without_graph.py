#AoC day_23
import collections as c



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(list(line.strip()))
        f.close()
    return lines


#part_1
def calc_number_of_end_positions(trails, start):
    routes, vectors, route_lengths = c.deque(), {(1, 0): ('v', '.'), (-1, 0): ('.'), (0, 1): ('>', '.'), (0, -1): ('<', '.')}, []
    routes.append((start, 0, [start]))
    while routes:
        (y, x), steps, path = routes.pop()
        if (y, x) == (len(trails)-1, len(trails)-2):
            route_lengths.append(steps)
        for v in vectors.keys():
            n_y, n_x = y+v[0], x+v[1]
            if len(trails) > n_y > 0 and trails[n_y][n_x] in vectors[v] and (n_y, n_x) not in path:
                routes.appendleft(((n_y, n_x), steps+1, path + [(n_y, n_x)]))
    return route_lengths[-1]


#main
if __name__ == '__main__':
    trails = input_from_file("day_23/input.txt")
    print(calc_number_of_end_positions(trails, (0, 1)))
