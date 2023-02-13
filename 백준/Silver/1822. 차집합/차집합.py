n1, n2 = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

ab = setA - setB
ba = setB - setA

result = sorted(list(ab))

print(len(result))
if len(result):
    print(*result)