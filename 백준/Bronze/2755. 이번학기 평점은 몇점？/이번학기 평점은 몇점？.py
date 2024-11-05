score = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
}

n = int(input())
result = 0.0
total = 0

for i in range(n):
    ipt = input().split()
    result += int(ipt[1]) * score[ipt[2]]
    total += int(ipt[1])

print(f"{result / total + 10**-10:.2f}")
