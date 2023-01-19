eight = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 0: 'h'}
n = int(input())

print(eight[n % 8], end = '')
print((n - 1) // 8 + 1)