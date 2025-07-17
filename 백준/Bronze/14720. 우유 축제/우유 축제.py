n = int(input())
store = list(map(int, input().split()))

milk = 0
result = 0

for i in range(n):
    if store[i] == milk:
        milk = (milk + 1) % 3
        result += 1

print(result)
