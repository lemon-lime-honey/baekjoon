while True:
    try:
        n, m = input().split()
        result = 0

        for i in range(int(n), int(m) + 1):
            if len(str(i)) == len(set(str(i))):
                result += 1

        print(result)
    except:
        break
