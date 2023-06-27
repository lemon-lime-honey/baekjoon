n = int(input())
balls = input()
r, b = 0, 0
lchange, rchange = 0, 0

for ball in balls:
    if ball == 'R': r += 1
    else: b += 1

result = min(r, b)

for i in range(n):
    if balls[i] != balls[0]: break
    lchange += 1

if balls[0] == 'R': result = min(result, r - lchange)
else: result = min(result, b - lchange)

for i in range(n - 1, -1, -1):
    if balls[i] != balls[-1]: break
    rchange += 1

if balls[-1] == 'R': result = min(result, r - rchange)
else: result = min(result, b - rchange)

print(result)