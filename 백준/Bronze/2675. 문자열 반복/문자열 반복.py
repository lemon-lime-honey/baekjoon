t = int(input())

for i in range(t):
    r, s = map(str, input().split())
    for letter in s:
        print(letter * int(r), end = '')
    print()