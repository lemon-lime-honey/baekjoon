a, b, c = map(int, input().split())

if (a == b) * (c != a):
    print('C')
elif (b == c) * (a != b):
    print('A')
elif (c == a) * (b != c):
    print('B')
else:
    print('*')