while True:
    n = int(input())
    if n == -1:
        break
    factor = list()
    
    for i in range(1, n):
        if not (n % i):
            factor.append(i)
    
    if sum(factor) == n:
        print(f'{n} = ', end = '')
        print(*factor, sep = ' + ')
    else:
        print(f'{n} is NOT perfect.')