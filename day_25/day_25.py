#AoC day_25
import collections as c


#input
def input_from_file(file):
    lines = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().split(': ')
            lines[line[0]] = line[1].split() if line[0] not in lines else lines[line[0]] + line[1].split()
            for i in line[1].split(): lines[i] = [line[0]] if i not in lines else lines[i] + [line[0]]
        f.close()
    return lines


#part_1
#part_2
def get_groups(components, start_node):
    cur_nodes, group_a, start_node = c.deque(), set(), list(components.keys())[0]
    cur_nodes.append(start_node)
    group_a.add(start_node)
    while cur_nodes:
        node = cur_nodes.pop()
        for new_node in components[node]:
            if new_node in group_a: continue
            blocked, goal_entries = [], []
            for _ in range(4):
                if is_path(components, blocked, goal_entries, new_node, start_node): path = get_shortest_path(components, blocked, goal_entries, new_node, start_node)
                else: break
                blocked.extend(path)
                goal_entries.append(path[-1])
            else:
                group_a.add(new_node)
                cur_nodes.appendleft(new_node)
    return len(group_a) * (len(components) - len(group_a))

def is_path(components, blocked, goal_entries, start, goal):
    nodes, visited = c.deque(), set()
    nodes.append(start)
    while nodes:            
        node = nodes.pop()
        for new_node in components[node]:
            if new_node == goal and node not in goal_entries: return True
            if new_node not in visited and new_node not in blocked and new_node != goal:
                nodes.append(new_node)
                visited.add(new_node)
    return False

def get_shortest_path(components, blocked, goal_entries, start, goal):
    paths = c.deque()
    paths.append([start])
    while paths:
        path = paths.pop()
        for new_node in components[path[-1]]:
            if new_node == goal and path[-1] not in goal_entries: return path
            if new_node not in blocked and new_node not in path and new_node != goal: paths.appendleft(path + [new_node])


#main
if __name__ == '__main__':
    components = input_from_file("day_25/input.txt")
    start_node = list(components.keys())[0]
    print(get_groups(components, start_node))
