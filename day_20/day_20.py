#AoC day_20
import collections as c, math



#input
def input_from_file(file):
    lines = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().split(' -> ')
            if line[0][0] == '%': lines[line[0][1:]] = [line[0][0], line[1].split(', '), False]
            elif line[0][0] == '&': lines[line[0][1:]] = [line[0][0], line[1].split(', '), {}]
            else: lines[line[0]] = ['cast', line[1].split(', ')]
        for i in lines.items():
            for j in i[1][1]:
                if j in lines and lines[j][0] == '&': lines[j][2][i[0]] = False
        f.close()
    return lines


#part_1
#part_2
def calc_pulses_or_minimal_presses_for_activation(modules, final_module, part2):
    presses, low_pulses, high_pulses = 1000 if not part2 else 10000, 0, 0
    origins = {name: None for name in modules[final_module][2].keys()}
    for i in range(presses):
        cycle = c.deque()
        cycle.append(['broadcaster', False, None])
        while cycle:
            dest, pulse, origin = cycle.pop()
            if pulse: high_pulses += 1
            else: low_pulses += 1
            if dest == final_module and pulse and not origins[origin]: origins[origin] = i + 1
            if dest not in modules: continue
            module = modules[dest]
            if module[0] == 'cast': target_pulse = pulse
            elif module[0] == '&':
                module[2][origin] = pulse
                target_pulse = not all(origin_pulse for origin_pulse in module[2].values())
            elif module[0] == '%' and pulse == False:
                module[2] = not module[2]
                target_pulse = module[2]
            else: continue
            cycle.extendleft([[target, target_pulse, dest] for target in module[1]])
    return low_pulses * high_pulses if not part2 else math.lcm(*origins.values())


#main
if __name__ == '__main__':
    for part in (False, True):
        modules = input_from_file("day_20/input.txt")
        print(calc_pulses_or_minimal_presses_for_activation(modules, 'vr', part))
