k = abs(int(input()))

if k == 0: print(0)
elif k % 2 == 0: print(-1)
else:
    reach = 1
    result = 0

    while k > 0:
        k -= reach
        reach *= 2
        result += 1

    print(result)
