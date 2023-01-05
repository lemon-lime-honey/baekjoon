import sys

for i in range(3):
    n = int(sys.stdin.readline())
    addi = 0
    for j in range(n):
        addi += int(sys.stdin.readline())
    if addi == 0:
        print('0')
    elif addi > 0:
        print('+')
    else:
        print('-')
