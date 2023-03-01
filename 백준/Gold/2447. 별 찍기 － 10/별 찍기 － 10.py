def star(n):
    if n == 1:
        return ['*']
    
    temp = star(n // 3)
    result = list()

    for element in temp:
        result.append(element * 3)
    for element in temp:
        result.append(element + ' ' * (n // 3) + element)
    for element in temp:
        result.append(element * 3)
    return result

n = int(input())
print('\n'.join(star(n)))