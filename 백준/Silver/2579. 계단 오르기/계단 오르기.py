import sys

n = int(sys.stdin.readline())
stair = [0] * n
score = [0] * n

for i in range(n):
    score[i] = int(sys.stdin.readline())

if len(score) < 3:
    print(sum(score))
else:
    stair[0] = score[0]
    stair[1] = max(score[0] + score[1], score[1])
    
    for i in range(2, n):
        stair[i] = max(stair[i - 3] + score[i - 1] + score[i], stair[i - 2] + score[i])
    
    print(stair[-1])