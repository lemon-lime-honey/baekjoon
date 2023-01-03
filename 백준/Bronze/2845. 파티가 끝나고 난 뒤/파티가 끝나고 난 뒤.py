l, p = map(int, input().split())
people = list(map(int, input().split()))
result = list()
real = l * p

for num in people:
    result.append(str(num - real))

print(' '.join(result))