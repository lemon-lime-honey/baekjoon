a, b = map(int, input().split())
m = int(input())
original = list(map(int, input().split()))
original.reverse()
decimal = 0

for i in range(len(original)):
    decimal += original[i] * (a ** i)

result = list()

while decimal // b:
    result.append(decimal % b)
    decimal //= b

result.append(decimal)

print(*result[::-1])