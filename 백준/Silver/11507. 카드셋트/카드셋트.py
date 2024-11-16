import sys

input = sys.stdin.readline


def calc():
    s = input().rstrip()
    result = [13 for i in range(4)]
    seen = set()

    for i in range(0, len(s), 3):
        if s[i: i + 3] in seen:
            print("GRESKA")
            return
        seen.add(s[i: i + 3])
        result["PKHT".index(s[i])] -= 1

    print(*result)


calc()
