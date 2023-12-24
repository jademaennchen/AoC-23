#AoC day_17
from collections import deque



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(list(map(int, list(line.strip()))))
        f.close()
    return lines


#part_1
#part_2
def calc_lowest_heat_loss(city_blocks, ultra_crucibles):
    visited, to_scan = {((0, 0), (0, 0), 0): 0}, deque()
    to_scan.append(((0, 0), (0, 0), 0, 0))
    vectors, best_heat = ((1, 0), (-1, 0), (0, 1), (0, -1)), float('inf')
    while to_scan:
        pos, cur_v, v_len, dist = to_scan.pop()
        if pos == (len(city_blocks) - 1, len(city_blocks[0]) - 1) and dist < best_heat and (not ultra_crucibles or v_len > 3): best_heat = dist
        for new_v in vectors:
            new_pos = (pos[0] + new_v[0], pos[1] + new_v[1])
            if len(city_blocks) > new_pos[0] > -1 and len(city_blocks[0]) > new_pos[1] > -1 and new_v != (-cur_v[0], -cur_v[1]):
                new_dist, new_len = dist + city_blocks[new_pos[0]][new_pos[1]], 1 if new_v != cur_v else v_len + 1
                valid = True if not ultra_crucibles and 0 < new_len < 4 else False
                valid_ultra = True if ultra_crucibles and 0 < new_len < 11 and ((cur_v != new_v and v_len > 3) or cur_v == new_v or cur_v == (0, 0)) else False
                key = ((new_pos[0], new_pos[1]), new_v, new_len, new_dist)
                if new_len != 0 and (key[:-1] not in visited or visited[key[:-1]] > new_dist) and (valid or valid_ultra):
                    to_scan.appendleft(key)
                    visited[key[:-1]] = new_dist
    return best_heat


#main
if __name__ == '__main__':
    city_blocks = input_from_file("day_17/input.txt")
    print(calc_lowest_heat_loss(city_blocks, False))
    print(calc_lowest_heat_loss(city_blocks, True))
