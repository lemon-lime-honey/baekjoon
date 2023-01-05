import sys

while True:
    line = sys.stdin.readline().strip()
    if line == 'END':
        break
    else:
        for i in range(len(line) - 1, -1, -1):
            print(line[i], end = '')
        print()