candy = list(map(int, input().split()))
candy.sort()
result = 2 * candy[2] - candy[0] - candy[1]
print(result)