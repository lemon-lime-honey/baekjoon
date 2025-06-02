while True:
    try:
        n = int(input())
        target = 1
        while True:
            if target % n == 0:
                print(len(str(target)))
                break
            target = target * 10 + 1
    except:
        break
