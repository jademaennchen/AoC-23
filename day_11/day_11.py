#AoC day_10
import numpy as np



#input
def input_from_file(file):
    lines = np.array([['' for _ in range(140)] for _ in range(140)])
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            lines[:, i] = list(line.strip())
        f.close()
    return lines
    

#part_1
def calc_sum_of_distances(image):
    running_sum = 0
    for i in reversed(range(len(image))):
        if all(c == '.' for c in image[:, i]): image = np.concatenate((image[:, 0:i], image[:, i:i+1], image[:, i:len(image[0])]), axis=1)
        if all(c == '.' for c in image[i, :]): image = np.concatenate((image[0:i, :], image[i:i+1, :], image[i:len(image), :]), axis=0)
    galaxies = [(x, y) for y in range(len(image[0])) for x in range(len(image)) if image[x, y] == '#']
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i + 1:]:
            running_sum += abs(g2[0] - g1[0]) + g2[1] - g1[1]
    return running_sum


#part_2
def calc_sum_of_distances_with_expansion(image):
    galaxies, running_sum = [[x, y] for y in range(len(image[0])) for x in range(len(image)) if image[x, y] == '#'], 0
    for i in reversed(range(len(image))):
        if all(c == '.' for c in image[:, i]):
            for galaxy in galaxies:
                if galaxy[1] > i: galaxy[1] += 999999
        if all(c == '.' for c in image[i, :]):
            for galaxy in galaxies:
                if galaxy[0] > i: galaxy[0] += 999999
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i + 1:]:
            running_sum += abs(g2[0] - g1[0]) + g2[1] - g1[1]
    return running_sum


#main
if __name__ == '__main__':
    image = input_from_file("day_11/input.txt")
    print(calc_sum_of_distances(image))
    print(calc_sum_of_distances_with_expansion(image))
