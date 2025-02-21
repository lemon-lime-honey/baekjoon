n = int(input())
result = 0

for i in range(n):
    x, y = map(int, input().split())
    match x:
        case 136:
            result += 1000
        case 142:
            result += 5000
        case 148:
            result += 10000
        case 154:
            result += 50000

print(result)
