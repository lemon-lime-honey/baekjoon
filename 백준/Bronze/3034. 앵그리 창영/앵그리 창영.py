n, w, h = map(int, input().split())
limit = (w**2 + h**2) ** 0.5

for i in range(n):
    if int(input()) <= limit:
        print("DA")
    else:
        print("NE")
