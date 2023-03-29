tc = int(input())

for i in range(tc):
    ipt = input()
    result = 0

    if ipt[0] == '1':
        result += 1
    
    for j in range(1, len(ipt)):
        if ipt[j] != ipt[j - 1]:
            result += 1

    print(f'#{i + 1} {result}')