t = int(input())

for i in range(t):
    temp = input()
    m = int(temp[4:6])
    d = int(temp[6:])

    if (m in (1, 3, 5, 7, 8, 10, 12)) * (d in range(1, 32)) + (m in (4, 6, 9, 11)) * (d in range(1, 32)) + (m == 2) * (d in range(1,29)):
       print(f'#{i + 1} {temp[:4]}/{temp[4:6]}/{temp[6:]}')
    else:
       print(f'#{i + 1} -1')