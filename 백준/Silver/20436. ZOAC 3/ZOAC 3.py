left = {'q': (0, 0), 'w': (0, 1),
        'e': (0, 2), 'r': (0, 3),
        't': (0, 4), 'a': (1, 0),
        's': (1, 1), 'd': (1, 2),
        'f': (1, 3), 'g': (1, 4),
        'z': (2, 0), 'x': (2, 1),
        'c': (2, 2), 'v': (2, 3)}
right = {'y': (0, 5), 'u': (0, 6),
         'i': (0, 7), 'o': (0, 8),
         'p': (0, 9), 'h': (1, 5),
         'j': (1, 6), 'k': (1, 7),
         'l': (1, 8), 'b': (2, 4),
         'n': (2, 5), 'm': (2, 6)}

l, r = input().split()
string = input()
time = 0

pos = [[left[l][0], left[l][1]], [right[r][0], right[r][1]]]
target = list()

for letter in string:
    if letter in left:
        target = [left[letter][0], left[letter][1]]
        time += abs(pos[0][0] - target[0]) + abs(pos[0][1] - target[1]) + 1
        pos[0] = target
    else:
        target = [right[letter][0], right[letter][1]]
        time += abs(pos[1][0] - target[0]) + abs(pos[1][1] - target[1]) + 1
        pos[1] = target

print(time)