from collections import Counter

while True:
    try:
        a = Counter(input())
        b = Counter(input())

        aSet = set([x[0] for x in a.keys()])
        bSet = set([x[0] for x in b.keys()])
        intersect = aSet.intersection(bSet)

        result = list()
        
        for letter in intersect:
            result.append(letter * min(a[letter], b[letter]))

        result.sort()

        print(''.join(result))
    except:
        break