n = int(input())
s = input()
result = 0
bonus = 0

for i in range(1, n + 1):
    match s[i - 1]:
        case "O":
            result += i + bonus
            bonus += 1
        case "X":
            bonus = 0

print(result)
