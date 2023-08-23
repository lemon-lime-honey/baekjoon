n = int(input())
loss = list(map(int, input().split()))
loss.sort()
result = 0

if n % 2:
    for i in range(n // 2 - 1):
          result = max(result, loss[i] + loss[n - 2 - i])
    result = max(result, loss[-1])
else:
   for i in range(n // 2):
      result = max(result, loss[i] + loss[n - 1 - i])

print(result)