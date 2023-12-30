#AoC day_21
import collections as c



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(list(line.strip()))
        f.close()
    return lines, len(lines)


#part_1
def calc_end_positions_or_steps_for_traversal(garden, start, goal, part2):
    positions, saved, vectors = c.deque(), {start[:-1]: True}, ((1, 0), (-1, 0), (0, 1), (0, -1))
    end_positions, valid_steps = 0, []
    positions.append(start)
    while positions:
        y, x, steps = positions.pop()
        if (goal - steps) % 2 == 0 and not part2: end_positions += 1
        if (goal - steps) % 2 == 0 and part2: valid_steps.append(steps)
        if not part2 and steps == goal: continue
        for d_y, d_x in vectors:
            new_y, new_x, new_entry = y+d_y, x+d_x, (y+d_y, x+d_x, steps + 1)
            if len(garden) > new_y >= 0 and len(garden) > new_x >= 0 and garden[new_y][new_x] != '#' and new_entry[:-1] not in saved:
                saved[new_entry[:-1]] = True
                positions.appendleft(new_entry)
    if not part2: return end_positions
    return max(valid_steps)


#part_2
def calc_end_positions_for_infinite_map(garden, steps):
    running_sum, full, half, max_fields_traveled = 0, len(garden) - 1, len(garden) // 2, steps // len(garden)
    entry_even, entry_odd = calc_end_positions_or_steps_for_traversal(garden, (0, half, 0), 0, True), calc_end_positions_or_steps_for_traversal(garden, (0, half, 0), 1, True)
    ring, even_entry_gardens, odd_entry_gardens, steps_left = 1, 1 if steps % 2 == 1 else 0, 1 if steps % 2 == 0 else 0, steps - half - 1
    while (steps_left >= entry_odd and steps_left % 2 == 1) or (steps_left >= entry_even and steps_left % 2 == 0):
        if steps_left % 2 == 1: odd_entry_gardens += ring * 4
        else: even_entry_gardens += ring * 4
        steps_left -= len(garden)
        ring += 1
    types = [((0, half, 0), entry_even, even_entry_gardens), ((0, half, 0), entry_odd, odd_entry_gardens)]
    types.extend([(i, steps_left, 1) for i in ((0, half, 0), (full, half, 0), (half, 0, 0), (half, full, 0))])
    if steps_left >= len(garden): types.extend([(i, steps_left - len(garden), 1) for i in ((0, half, 0), (full, half, 0), (half, 0, 0), (half, full, 0))])
    if steps_left - half - 1 >= 0: types.extend([(i, steps_left - half - 1, max_fields_traveled) for i in ((0, 0, 0), (full, 0, 0), (0, full, 0), (full, full, 0))])
    types.extend([(i, steps_left + half, max_fields_traveled - 1) for i in ((0, 0, 0), (full, 0, 0), (0, full, 0), (full, full, 0))])
    for type in types:
        running_sum += calc_end_positions_or_steps_for_traversal(garden, type[0], type[1], False) * type[2]
    return running_sum


#main
if __name__ == '__main__':
    garden, dim = input_from_file("day_21/input.txt")
    print(calc_end_positions_or_steps_for_traversal(garden, (dim // 2, dim // 2, 0), 64, False))
    print(calc_end_positions_for_infinite_map(garden, 26501365))
