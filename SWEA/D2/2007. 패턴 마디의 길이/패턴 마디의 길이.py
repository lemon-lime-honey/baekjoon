t = int(input())

for i in range(t):
    string = input()
    pattern = list()
    ref = 0
    while True:
        pattern.append(string[ref])
        if string[len(pattern):2 * len(pattern)] == ''.join(pattern):
            break
        ref += 1
    print(f'#{i + 1} {len(pattern)}')