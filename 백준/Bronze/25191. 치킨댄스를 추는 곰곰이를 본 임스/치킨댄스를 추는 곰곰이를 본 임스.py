n = int(input())
a, b = map(int, input().split())
calc = a // 2 + b
print(min(n, calc))