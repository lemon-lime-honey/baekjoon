x, y = map(int, input().split())
minimum = x * 1000 / y

n = int(input())
for i in range(n):
    temp1, temp2 = map(int, input().split())
    temp = temp1 * 1000 / temp2
    if temp < minimum:
        minimum = temp

print(f'{minimum:.2f}')