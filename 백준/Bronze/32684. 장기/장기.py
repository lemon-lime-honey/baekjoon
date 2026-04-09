score = [13, 7, 5, 3, 3, 2]
c, e = 0, 1.5

ipt = list(map(int, input().split()))
target = zip(score, ipt)
c += sum([t[0] * t[1] for t in target])

ipt = list(map(int, input().split()))
target = zip(score, ipt)
e += sum([t[0] * t[1] for t in target])

if c > e:
    print("cocjr0208")
else:
    print("ekwoo")
