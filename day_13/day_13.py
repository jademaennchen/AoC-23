#AoC day_13
import numpy as np



#input
def input_from_file(file):
    lines, current = [], []
    with open(file) as f:
        for line in f.readlines():
            if line.strip() != '': current.append(list(line.strip()))
            else:
                lines.append(np.array(current))
                current = []
        lines.append(np.array(current))
        f.close()
    return lines


#part_1
def calc_sum_of_notes(notes):
    running_sum = 0
    for note in notes:
        running_sum += find_mirror_from_note(note)
    return running_sum

def find_mirror_from_note(note):
    for i in range(len(note) - 1):
        if all("".join(note[i - k]) == "".join(note[i + 1 + k]) for k in range(min(i, len(note) - 2 - i) + 1)): return 100 * (i + 1)
    for j in range(len(note[0]) - 1):
        if all("".join(note[:, j - l]) == "".join(note[:, j + 1 + l]) for l in range(min(j, len(note[0]) - 2 - j) + 1)): return j + 1


#part_2
def calc_sum_of_notes_with_smudges(notes):
    running_sum = 0
    for note in notes:
        running_sum += find_mirror_from_note_with_smudges(note)
    return running_sum

def find_mirror_from_note_with_smudges(note):
    for i in range(len(note) - 1):
        smudges = 0
        for j in range(min(i, len(note) - 2 - i) + 1):
            count = sum([1 for k in range(len(note[0])) if note[i - j, k] != note[i + 1 + j, k]])
            if count == 1: smudges += 1
            elif count > 1: break
        else:
            if smudges == 1: return 100 * (i + 1)
    for l in range(len(note[0]) - 1):
        smudges = 0
        for m in range(min(l, len(note[0]) - 2 - l) + 1):
            count = sum([1 for n in range(len(note)) if note[n, l - m] != note[n, l + 1 + m]])
            if count == 1: smudges += 1
            elif count > 1: break
        else:
            if smudges == 1: return l + 1


#main
if __name__ == '__main__':
    notes = input_from_file("day_13/input.txt")
    print(calc_sum_of_notes(notes))
    print(calc_sum_of_notes_with_smudges(notes))
