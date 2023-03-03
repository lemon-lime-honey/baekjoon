seq = [1, 1, 1]

for i in range(113):
    seq.append(seq[-1] + seq[-3])

n = int(input())
print(seq[n - 1])