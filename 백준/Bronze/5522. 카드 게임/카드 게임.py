import sys

result = 0

while True:
    try:
        result += int(sys.stdin.readline())
    except:
        break

print(result)