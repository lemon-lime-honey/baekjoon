def dfs(index):
    global result, total
    if sum(total) == s and len(total):
        result += 1
    for i in range(index, n):
        total.append(number[i])
        dfs(i + 1)
        total.pop()
        
n, s = map(int, input().split())
number = list(map(int, input().split()))
total = list()
result = 0

dfs(0)

print(result)