s = int(input())
a, f, b = map(int, input().split())

if s <= 240 or s <= a + f + b:
    print("high speed rail")
else:
    print("flight")
