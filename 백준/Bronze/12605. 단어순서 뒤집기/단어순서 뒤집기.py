n = int(input())
words = list()

for i in range(n):
    words = list(map(str, input().split()))
    print(f'Case #{i + 1}: ', end = '')
    for j in range(len(words) - 1, -1, -1):
        print(words[j], end = ' ')
    print()