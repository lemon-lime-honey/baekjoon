import sys

input = sys.stdin.readline

while True:
    n, w = map(int, input().split())

    if n == w == 0:
        break

    sticks = sorted([int(input()) for i in range(n)], reverse=True)
    numDict = dict()

    upper = w

    numDict[(0, w)] = 0

    while upper <= sticks[0]:
        numDict[(upper, upper + w)] = 0
        upper += w

    for stick in sticks:
        for lower, upper in numDict.keys():
            if lower <= stick < upper:
                numDict[(lower, upper)] += 1
                break

    histogram = [x[1] for x in sorted(numDict.items(), key=lambda x: -x[0][0])]
    tallest = max(histogram)
    result = 0.01
    ink = 0

    for idx, cnt in enumerate(histogram):
        result += cnt / tallest * ink
        ink += 1 / (len(histogram) - 1)

    print(result)
