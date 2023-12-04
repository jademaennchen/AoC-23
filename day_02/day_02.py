#AoC Day 02



#input
def input_from_file(file):
    lines = []
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            lines += [[j.split(" ") for j in line.strip().replace("Game " + str(i + 1) + ": ", "").replace('; ', ", ").split(", ")]]
        f.close()
    return lines


#part_1
def calc_sum_of_valid_games(games):
    running_sum = 0
    for i, game in enumerate(games):
        if is_valid_game(game): running_sum += i+1
    return running_sum

def is_valid_game(game):
    for reveal in game:
        if((reveal[1] == "red" and int(reveal[0]) > 12) or (reveal[1] == "green" and int(reveal[0]) > 13) or (reveal[1] == "blue" and int(reveal[0]) > 14)): return False
    return True


#part_2
def calc_sum_of_powers_of_minimum_cube_games(games):
    running_sum = 0
    for game in games:
        running_sum += calc_game_power(game)
    return running_sum

def calc_game_power(game):
    max_red, max_green, max_blue = 0, 0, 0
    for reveal in game:
        if(reveal[1] == "red"): max_red = max(max_red, int(reveal[0]))
        elif(reveal[1] == "green"): max_green = max(max_green, int(reveal[0]))
        elif(reveal[1] == "blue"): max_blue = max(max_blue, int(reveal[0]))
    return max_red * max_green * max_blue


#main
if __name__ == '__main__':
    games = input_from_file("day_02/input.txt")
    print(calc_sum_of_valid_games(games))
    print(calc_sum_of_powers_of_minimum_cube_games(games))
