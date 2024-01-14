#AoC day_24
import numpy as np


#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append([list(map(int, j.split(', '))) for j in line.strip().split(' @ ')])
        f.close()
    return lines


#part_1
def calc_intersections(hailstones):
    intersections = 0
    for i, hail in enumerate(hailstones):
        for checked_hail in hailstones[i+1:]:
            (p1, v1), (p2, v2) = hail , checked_hail
            coefficients, values = [[v1[0], -v2[0]], [v1[1], -v2[1]]], [[p2[0] - p1[0]], [p2[1] - p1[1]]]
            sol1, sol2 = [sol[0] for sol in np.linalg.solve(coefficients, values)] if v1[0] / v2[0] != v1[1] / v2[1] else [0, 0]
            if sol1 > 0 and sol2 > 0 and 2*10**14 <= p1[0] + v1[0] * sol1 <= 4*10**14 and 2*10**14 <= p1[1] + v1[1] * sol1 <= 4*10**14: intersections += 1
    return intersections


#part2
def calc_rock_throw(hailstones):
    vel = []
    for ax in range(3):
        for r_vel in range(-400, 400):
            for (p1, v1), (p2, v2) in [(h1, h2) for i, h1 in enumerate(hailstones, 1) for h2 in hailstones[i:] if h1 != h2 and h1[1][ax] == h2[1][ax]]:
                p_dif, v_dif = abs(p2[ax]-p1[ax]), abs(r_vel - v2[ax])
                if v_dif == 0 or p_dif % v_dif != 0: break
            else:
                vel.append(r_vel)
                break
    cur_a, cur_b = hailstones[0], hailstones[-1]
    p1, v1, p2, v2 = cur_a[0], [cur_a[1][0]-vel[0], cur_a[1][1]-vel[1], cur_a[1][2]-vel[2]], cur_b[0], [cur_b[1][0]-vel[0], cur_b[1][1]-vel[1], cur_b[1][2]-vel[2]]
    coefficients, values = [[v1[0], -v2[0], 1], [v1[1], -v2[1], 2], [v1[2], -v2[2], 3]], [[p2[0] - p1[0] + 1], [p2[1] - p1[1] + 2], [p2[2] - p1[2] + 3]]
    sol = [int(sol[0]) for sol in np.linalg.solve(coefficients, values)][0]
    throw_coords = [p1[0]+v1[0]*sol, p1[1]+v1[1]*sol, p1[2]+v1[2]*sol]
    return sum(throw_coords)


#main
if __name__ == '__main__':
    hailstones = input_from_file("day_24/input.txt")
    print(calc_intersections(hailstones))
    print(calc_rock_throw(hailstones))
