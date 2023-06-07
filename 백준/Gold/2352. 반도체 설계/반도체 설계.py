from bisect import bisect_left

n = int(input())
port = list(map(int, input().split()))

result = [port[0]]

for i in range(1, n):
    if result[-1] < port[i]:
        result.append(port[i])
    else:
        result[bisect_left(result, port[i])] = port[i]

print(len(result))