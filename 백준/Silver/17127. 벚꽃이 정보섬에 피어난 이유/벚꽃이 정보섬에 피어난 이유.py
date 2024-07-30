n = int(input())
flowers = list(map(int, input().split()))

result = 0
first = 1

for i in range(n - 3):
    first *= flowers[i]
    second = 1
    for j in range(i + 1, n - 2):
        second *= flowers[j]
        third = 1
        for k in range(j + 1, n - 1):
            third *= flowers[k]
            fourth = 1
            for l in range(k + 1, n):
                fourth *= flowers[l]
            result = max(result, first + second + third + fourth)

print(result)
