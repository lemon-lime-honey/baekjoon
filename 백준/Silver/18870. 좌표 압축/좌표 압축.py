n = int(input())
original = list(map(int, input().split()))
dict_n = {x: 0 for x in sorted(original, reverse = True)}
key_n = list(dict_n.keys())
result = list()

for index, value in enumerate(key_n):
    dict_n[value] = len(key_n) - index - 1

for num in original:
    result.append(dict_n[num])

print(*result)