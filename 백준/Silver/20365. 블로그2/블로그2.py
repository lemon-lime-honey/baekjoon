n = int(input())
colors = input()
b, r = 0, 0

if colors[0] == 'B': b += 1
else: r += 1

for i in range(n - 1):
    if colors[i] != colors[i + 1]:
        if colors[i + 1] == 'B': b += 1
        else: r += 1

print(min(r + 1, b + 1))