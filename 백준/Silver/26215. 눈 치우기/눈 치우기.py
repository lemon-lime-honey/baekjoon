n = int(input())
snow = list(map(int, input().split()))
result = 0

while n != 1:
    snow.sort(reverse=True)
    if snow[1] == 0:
        break
    snow[0] -= 1
    snow[1] -= 1
    result += 1

result += snow[0]

print(result if result <= 1440 else -1)
