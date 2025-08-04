b = list(map(int, input().split()))
d = list(map(int, input().split()))
j = list(map(int, input().split()))

bessie = max(abs(b[0] - j[0]), abs(b[1] - j[1]))
daisy = abs(d[0] - j[0]) + abs(d[1] - j[1])

if bessie < daisy:
    print("bessie")
elif bessie == daisy:
    print("tie")
else:
    print("daisy")
