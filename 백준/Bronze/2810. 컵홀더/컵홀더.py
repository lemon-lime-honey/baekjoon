n = int(input())
seats = input()
result = 0
idx = 0

while idx < n:
    result += 1
    if seats[idx] == 'L':
        idx += 2
    else:
        idx += 1

print(min(result + 1, n))