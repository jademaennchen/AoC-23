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
def calc_longest_path(trails, start_pos, goal, part2):
    routes, vectors, paths, sections = c.deque(), {(1, 0): ('v', '.'), (-1, 0): ('.'), (0, 1): ('>', '.'), (0, -1): ('<', '.')}, [], {}
    if part2:
        routes.extend([((y, x), [(y, x)]) for y in range(1, len(trails)-1) for x in range(1, len(trails)-1) if sum(trails[y+v[0]][x+v[1]] != '#' for v in vectors.keys()) > 2] + [(start_pos, [start_pos]), (goal, [goal])])
        for route in routes: sections[route[0]] = []
    else: routes.append((start_pos, [start_pos]))
    while routes:
        (y, x), path = routes.pop()
        if part2 and len(path) > 1 and (y, x) in sections.keys():
            sections[path[0]].append(((y, x), len(path)-1))
            continue
        if not part2 and (y, x) == goal: paths.append((len(path)-1))
        for v in vectors.keys():
            n_y, n_x = y+v[0], x+v[1]
            allowed = ('v', '>', '<', '.') if part2 else vectors[v]
            if len(trails) > n_y > 0 and trails[n_y][n_x] in allowed and (n_y, n_x) not in path: routes.appendleft(((n_y, n_x), path + [(n_y, n_x)]))
    if not part2: return paths[-1]
    routes.append(((start_pos, ), 0))
    max_steps = 0
    while routes:
        path, steps = routes.pop()
        if path[-1] == goal:
            if steps > max_steps: max_steps = steps
            continue
        for new_pos, add_steps in sections[path[-1]]:
            if new_pos not in path: routes.appendleft((path + (new_pos, ), steps + add_steps))
    return max_steps


#main
if __name__ == '__main__':
    trails = input_from_file("day_23/input.txt")
    print(calc_longest_path(trails, (0, 1), (len(trails)-1, len(trails)-2), False))
    print(calc_longest_path(trails, (0, 1), (len(trails)-1, len(trails)-2), True))
