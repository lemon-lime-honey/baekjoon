t = int(input())

for i in range(t):
    k = int(input())
    word = set()
    result = None
    
    for j in range(k):
        ipt = input()
        if result:
            continue
        if word:
            for w in word:
                target = ipt + w
                if target == target[::-1]:
                    result = target
                    break
                target = w + ipt
                if target == target[::-1]:
                    result = target
                    break
        word.add(ipt)

    print(result if result else 0)
