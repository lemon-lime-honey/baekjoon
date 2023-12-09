def backtrack():
    global result
    temp = 0
    for num in route:
        temp = temp * 10 + num
    if temp > n: return

    result = max(result, temp)
    for num in nums:
        route.append(num)
        backtrack()
        route.pop()


n, k = map(int, input().split())
nums = list(map(int, input().split()))
route = list()
result = 0

backtrack()

print(result)