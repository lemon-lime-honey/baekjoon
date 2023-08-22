n = int(input())
drinks = sorted(list(map(float, input().split())))

for i in range(n - 1):
    drinks[-1] += drinks[i] / 2

print(drinks[-1])