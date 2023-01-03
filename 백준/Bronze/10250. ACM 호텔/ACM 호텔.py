t = int(input())

for i in range(0, t):
    h, w, n = map(int, input().split())

    if (n%h==0):
        y = h
        x = n//h
    else:
        y = n%h
        x = (n//h)+1

    print('{0}{1}'.format(y, str(x).zfill(2)))
