t = int(input())

for i in range(t):
    word = input()
    print(f'#{i + 1}', end = ' ')
    if word == word[::-1]:
        print(1)
    else:
        print(0)