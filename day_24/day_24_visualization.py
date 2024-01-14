#AoC day_24
import matplotlib.pyplot as plt


#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            line = [tuple(map(int, j.split(', '))) for j in line.strip().split(' @ ')]
            lines.append(line)
        f.close()
    return lines


#part2
def visualize_intersections(hailstones, j):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    for i, hail in enumerate(hailstones):
        (p1, v1) = hail
        pos = p1[j]
        ax.plot(pos, i, marker='x', color = 'k')
        while 7 <= pos + v1[j] <= 27:
            pos = pos + v1[j]
            ax.plot(pos, i, marker='x', color = colors[i])
        pos = 23
        vel = -3
        ax.plot(pos, 6, marker='x', color = 'k')
        ax.plot([pos, pos], [0, 6], color = 'k')
        while 7 <= pos + vel <=27:
            pos = pos + vel
            ax.plot(pos, 6, marker='x', color = 'y')
            ax.plot([pos, pos], [0, 6], color = 'y')
    plt.show()
    return 0


#main
if __name__ == '__main__':
    hailstones = input_from_file("day_24/input2.txt")
    print(visualize_intersections(hailstones, 0))
