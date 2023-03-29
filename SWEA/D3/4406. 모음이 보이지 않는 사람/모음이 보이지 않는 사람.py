tc = int(input())

for i in range(tc):
    ipt = input()
    result = list()

    for letter in ipt:
        if letter not in 'aeiou':
            result.append(letter)
    
    print(f'#{i + 1} {"".join(result)}')