import sys

input = sys.stdin.readline

n = int(input())
car_input = dict()
car_output = dict()
result = 0

for i in range(n):
    car_input[input().rstrip()] = i

for i in range(n):
    car_output[input().rstrip()] = i

for idx, car in enumerate(car_output.keys()):
    if idx == n - 1:
        break
    for i, c in enumerate(car_output.keys()):
        if i < idx + 1:
            continue
        if car_input[c] < car_input[car]:
            result += 1
            break

print(result)
