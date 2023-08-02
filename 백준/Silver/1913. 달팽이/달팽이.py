n = int(input())
target = int(input())

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
table = [[0 for i in range(n)] for j in range(n)]
ref = [n // 2, n // 2]
result = [n // 2 + 1, n // 2 + 1]

table[ref[0]][ref[1]] = 1
pos = [0, 0]
number = 2
turn = 0

for i in range(3, n + 1, 2):
    pos = ref
    pos = pos[0] + direction[turn][0], pos[1] + direction[turn][1]
    table[pos[0]][pos[1]] = number
    if number == target:
        result = pos[0] + 1, pos[1] + 1
    number += 1

    turn = 1
    for j in range(i - 2):
        pos = pos[0] + direction[turn][0], pos[1] + direction[turn][1]
        table[pos[0]][pos[1]] = number
        if number == target:
            result = pos[0] + 1, pos[1] + 1
        number += 1

    turn = 2
    for j in range(i - 1):
        pos = pos[0] + direction[turn][0], pos[1] + direction[turn][1]
        table[pos[0]][pos[1]] = number
        if number == target:
            result = pos[0] + 1, pos[1] + 1
        number += 1

    turn = 3
    for j in range(i - 1):
        pos = pos[0] + direction[turn][0], pos[1] + direction[turn][1]
        table[pos[0]][pos[1]] = number
        if number == target:
            result = pos[0] + 1, pos[1] + 1
        number += 1

    turn = 0
    for j in range(i - 1):
        pos = pos[0] + direction[turn][0], pos[1] + direction[turn][1]
        table[pos[0]][pos[1]] = number
        if number == target:
            result = pos[0] + 1, pos[1] + 1
        number += 1

    ref[0] -= 1
    ref[1] -= 1

for i in range(n):
    print(*table[i])

print(*result)