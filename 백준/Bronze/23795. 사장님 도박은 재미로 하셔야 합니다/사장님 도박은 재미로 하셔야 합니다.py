import sys

result = 0

while True:
    money = int(sys.stdin.readline())
    if money == -1:
        break
    result += money

print(result)