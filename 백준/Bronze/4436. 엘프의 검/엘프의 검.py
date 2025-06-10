from collections import Counter
import sys

input = sys.stdin.readline

while True:
    try:
        num = int(input())
        cnt = Counter()
        k = 1
        
        while True:
            target = num * k
            cnt.update(Counter(str(target)))
            if len(cnt) == 10:
                print(k)
                break
            k += 1
    except:
        break
