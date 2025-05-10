from collections import defaultdict
import sys

input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n, k = map(int, input().split())
    boards = input().split()
    board_dict = defaultdict(int)
    res = 0

    for board in boards:
        upper = 0
        for letter in board:
            if letter.isupper():
                upper += 1
        board_dict[("".join(sorted(board.lower())), upper)] += 1

    for value in board_dict.values():
        if value > 1:
            res += value * (value - 1) // 2

    result.append(res)

print(*result, sep="\n")
