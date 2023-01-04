n, w, h, l = map(int, input().split())
temp = (w // l) * (h // l)
if n < temp:
    print(n)
else:
    print(temp)