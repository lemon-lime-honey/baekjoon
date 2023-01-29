n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start = 1
end = tree[-1]

while start <= end:
    mid = (start + end) // 2
    length = 0

    for i in range(n):
        if tree[i] > mid:
            length += tree[i] - mid
    
    if length == m:
        end = mid
        break
    elif length < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)