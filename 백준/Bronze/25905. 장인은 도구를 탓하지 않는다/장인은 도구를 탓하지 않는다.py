probs = [float(input()) for i in range(10)]
probs.sort()
result = 1

for i in range(1, 10):
    result *= probs[i] / i

print(result * int(1e9))