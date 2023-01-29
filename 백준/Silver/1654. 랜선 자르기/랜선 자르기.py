import sys

k, n = map(int, sys.stdin.readline().split())
cable = list()
result = 0

for i in range(k):
    cable.append(int(sys.stdin.readline()))

cable.sort()
start = 1
end = cable[-1]

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(k):
        cnt += cable[i] // mid
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)