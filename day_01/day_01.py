#AoC Day 01



#input
def input_from_file(file):
    with open(file) as f:
        lines = f.readlines()
        f.close()
    return lines


#part 1
def calc_total_sum(lines):
    running_sum = 0
    for cur in lines:
        nums = [c for c in cur if c.isdigit()]
        running_sum += int(nums[0] + nums[-1])
    return running_sum


#part 2
def calc_total_sum_with_string_numbers(lines):
    running_sum = 0
    for cur in lines:
        running_sum += find_first_number(cur) * 10 + find_last_number(cur)
    return running_sum

def find_first_number(string):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(string)):
        for j, num in enumerate(nums + list(map(str, range(1, 10)))):
            if(num in string[0:i+1]): return j % 9 + 1
    return "0"

def find_last_number(string):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(string), 0, -1):
        for j, num in enumerate(nums + list(map(str, range(1, 10)))):
            if(num in string[i-1:len(string)]): return j % 9 + 1
    return "0"


#main
if __name__ == '__main__':
    lines = input_from_file("day_01/input.txt")
    print(calc_total_sum(lines))
    print(calc_total_sum_with_string_numbers(lines))
