#AoC day_16



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(list(line.strip()))
        f.close()
    return lines
    

#part_1
def calc_energized_tiles(grid, start):
    tiles, not_visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))], []
    not_visited.append(start)
    while not_visited:
        pos, vec = not_visited[0][0], not_visited[0][1]
        if len(grid) > pos[0] > -1 and len(grid[0]) > pos[1] > -1:
            if not tiles[pos[0]][pos[1]] or vec not in tiles[pos[0]][pos[1]]:
                tiles[pos[0]][pos[1]].append(vec)
                if grid[pos[0]][pos[1]] == '/': not_visited.append(((pos[0] - vec[1], pos[1] - vec[0]), (-vec[1], -vec[0])))
                elif grid[pos[0]][pos[1]] == '\\': not_visited.append(((pos[0] + vec[1], pos[1] + vec[0]), vec[::-1]))
                elif grid[pos[0]][pos[1]] == '|' and vec[0] == 0: not_visited.extend((((pos[0] + 1, pos[1]), (1, 0)), ((pos[0] - 1, pos[1]), (-1, 0))))
                elif grid[pos[0]][pos[1]] == '-' and vec[1] == 0: not_visited.extend((((pos[0], pos[1] + 1), (0, 1)), ((pos[0], pos[1] - 1), (0, -1))))
                else: not_visited.append(((pos[0] + vec[0], pos[1] + vec[1]), vec))
        not_visited = not_visited[1:]
    return sum([1 for y in range(len(grid)) for x in range(len(grid[0])) if tiles[y][x]])


#part_2
def calc_max_energized_tiles(grid):
    energy_values = []
    for i in range(len(grid)):
        energy_values.append(calc_energized_tiles(grid, ((i, 0), (0, 1))))
        energy_values.append(calc_energized_tiles(grid, ((i, len(grid[0]) - 1), (0, -1))))
    for j in range(len(grid[0])):
        energy_values.append(calc_energized_tiles(grid, ((0, j), (1, 0))))
        energy_values.append(calc_energized_tiles(grid, ((len(grid) - 1, j), (-1, 0))))
    return max(energy_values)


#main
if __name__ == '__main__':
    grid = input_from_file("day_16/input.txt")
    print(calc_energized_tiles(grid, ((0, 0), (0, 1))))
    print(calc_max_energized_tiles(grid))
