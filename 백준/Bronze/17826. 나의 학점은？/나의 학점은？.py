scores = list(map(int, input().split()))
score = int(input())

idx = scores.index(score)

if idx < 5:
    print("A+")
elif idx < 15:
    print("A0")
elif idx < 30:
    print("B+")
elif idx < 35:
    print("B0")
elif idx < 45:
    print("C+")
elif idx < 48:
    print("C0")
else:
    print("F")
