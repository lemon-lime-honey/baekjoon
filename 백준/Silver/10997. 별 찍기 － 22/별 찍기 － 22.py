def star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return ['*****', '*    ', '* ***', '* * *', '* * *', '*   *', '*****']
    before = star(n - 1)
    result = list()

    result.append('*' * (len(before[0]) + 4))
    result.append('*' + ' ' * (len(before[0]) + 3))

    for i in range(len(before)):
        if i == 0:
            result.append('* ' + before[i] + '**')
        else:
            result.append('* ' + before[i] + ' *')

    result.append('*' + ' ' * (len(before[0]) + 2) + '*')
    result.append('*' * (len(before[0]) + 4))

    return result


n = int(input())
answer = star(n)

for line in answer:
    print(*line.rstrip(), sep='')