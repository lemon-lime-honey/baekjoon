import sys
input = sys.stdin.readline


def search(route):
    if len(route) == len(ipt):
        result.add(''.join(route))
        return

    for i in range(26):
        if chk[i]:
            route.append(chr(i + ord('a')))
            chk[i] -= 1
            search(route)
            route.pop()
            chk[i] += 1


n = int(input())

for i in range(n):
    ipt = sorted(list(input().rstrip()))
    chk = [0 for i in range(26)]
    result = set()

    for letter in ipt:
        chk[ord(letter) - ord('a')] += 1

    search(list())

    print(*sorted(result), sep='\n')