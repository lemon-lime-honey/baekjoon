import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    s = input().rstrip()
    result = list()

    for letter in s:
        result.append(chr(ord("A") + (a * (ord(letter) - ord("A")) + b) % 26))

    print("".join(result))
