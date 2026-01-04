import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    msg = input().rstrip()
    maps = input().rstrip()

    result = list()

    for letter in msg:
        if letter == " ":
            result.append(letter)
        else:
            result.append(maps[ord(letter) - 65])

    print("".join(result))
