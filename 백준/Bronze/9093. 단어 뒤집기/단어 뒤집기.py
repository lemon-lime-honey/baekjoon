t = int(input())

for i in range(t):
    sentence = map(str, input().split())
    for word in sentence:
        print(word[::-1], end = ' ')
    print()