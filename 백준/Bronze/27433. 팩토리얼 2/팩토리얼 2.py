fact = [1]

for i in range(1, 21):
    fact.append(i * fact[-1])

n = int(input())
print(fact[n])