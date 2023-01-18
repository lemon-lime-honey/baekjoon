n = int(input())

for i in range(n):
    number, sect1, sect2, sect3 = map(int, input().split())
    total = sect1 + sect2 + sect3
    if (sect1 < (35 * 0.3)) + (sect2 < (25 * 0.3)) + (sect3 < (40 * 0.3)) + (total < 55):
        print(f'{number} {total} FAIL')
    else:
        print(f'{number} {total} PASS')