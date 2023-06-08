from bisect import bisect_left

n = int(input())
numbers = list(map(int, input().split()))
sub = [1 for i in range(n)]

result = [numbers[0]]

for i in range(1, n):
    if result[-1] < numbers[i]:
        result.append(numbers[i])
        sub[i] = len(result)
    else:
        idx = bisect_left(result, numbers[i])
        result[idx] = numbers[i]
        sub[i] = idx + 1

print(len(result))
ref = len(result)
answer = list()

for i in range(n - 1, -1, -1):
    if sub[i] == ref:
        answer.append(numbers[i])
        ref -= 1

print(*answer[::-1])