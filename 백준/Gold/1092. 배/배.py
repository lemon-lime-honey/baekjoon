import sys
input = sys.stdin.readline

n = int(input())
limit = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
weights = sorted(list(map(int, input().split())), reverse=True)

if limit[0] < weights[0]:
    print(-1)
else:
    result = 0
    while weights:
        for i in range(n):
            for j in range(len(weights)):
                if weights[j] <= limit[i]:
                    del weights[j]
                    break
        result += 1
    print(result)