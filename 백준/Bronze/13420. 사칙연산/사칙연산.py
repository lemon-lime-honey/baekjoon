t = int(input())

for i in range(t):
    ipt = input().replace(" ", "").split("=")
    print("correct" if eval(ipt[0]) == int(ipt[-1]) else "wrong answer")
