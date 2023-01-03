plus, minus = map(int, input().split())
if (plus < minus):
    print(-1)
else:
    n1 = (plus + minus) // 2
    n2 = (plus - minus) // 2
    if (n1 + n2 == plus):
        print(n1, n2)
    else:
        print(-1)