movement = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 
           'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

k, s, n = input().split()
king = [ord(k[0]), int(k[1])]
stone = [ord(s[0]), int(s[1])]
n = int(n)

for i in range(n):
    move = input()
    tempK = [king[0] + movement[move][0], king[1] + movement[move][1]]
    tempS = [stone[0] + movement[move][0], stone[1] + movement[move][1]]

    if (64 < tempK[0] < 73) and (0 < tempK[1] < 9):
        if (tempK[0] == stone[0]) and (tempK[1] == stone[1]):
            if not (64 < tempS[0] < 73) or not (0 < tempS[1] < 9):
                continue
            stone = tempS
        king = tempK

print(chr(king[0]), king[1], sep = '')
print(chr(stone[0]), stone[1], sep = '')