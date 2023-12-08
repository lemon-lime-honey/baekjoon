from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    
    score = defaultdict(int)
    
    for i in range(n):
        ipt = list(map(int, input().split()))
        for number in ipt:
            score[number] += 1

    result = sorted(score.items(), key=lambda x: (-x[1], x[0]))
    second = -1

    for i in range(1, len(result)):
        if result[i][1] < result[0][1]:
            if second == -1:
                second = result[i][1]
            elif second != result[i][1]:
                break
            print(result[i][0], end=' ')

    print()