import sys

input = sys.stdin.readline

now = list(map(float, input().split()))
target = list(map(float, input().split()))

result = [0.0 for i in range(5)]

for i in range(3, 5):
    result[i] = now[i] - (target[i] - now[i])

days_now = now[2] + now[1] * 30 + now[0] * 30 * 12
days_target = target[2] + target[1] * 30 + target[0] * 30 * 12

days_diff = days_target - days_now

days = days_now - days_diff

if days % 30:
    result[2] = days % 30
    days -= days % 30
else:
    result[2] = 30
    days -= 30

days //= 30

if days % 12:
    result[1] = days % 12
    days -= days % 12
else:
    result[1] = 12
    days -= 12

days //= 12

result[0] = days

print(f"{result[0]:.0f} {result[1]:.0f} {result[2]:.0f} {result[3]:.3f} {result[4]:.3f}")
