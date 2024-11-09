n = int(input())
score = sorted(list(map(int, input().split())))

print(score[-1] - score[0])