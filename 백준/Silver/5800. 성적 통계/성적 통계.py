import sys
input = sys.stdin.readline

k = int(input())

for i in range(1, k + 1):
    ipt = list(map(int, input().split()))
    n = ipt[0]
    score = sorted(ipt[1:], reverse=True)
    maximum, minimum, gap = score[-1], score[-1], 0

    for j in range(n - 1):
        maximum = max(maximum, score[j])
        minimum = min(minimum, score[j])
        gap = max(gap, score[j] - score[j + 1])

    print(f'Class {i}\nMax {maximum}, Min {minimum}, Largest gap {gap}')