from math import factorial

while True:
    try:
        n = int(input())
        fact = factorial(n)
        last = 0
        while True:
            if fact % 10 != 0:
                last = fact % 10
                break
            else:
                fact = fact // 10
        if n < 10:
            print(f'    {n} -> {last}')
        elif n < 100:
            print(f'   {n} -> {last}')
        elif n < 1000:
            print(f'  {n} -> {last}')
        else:
            print(f' {n} -> {last}')
    except:
        break