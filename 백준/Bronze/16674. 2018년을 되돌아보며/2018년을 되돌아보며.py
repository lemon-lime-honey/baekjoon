from collections import Counter

cnt = Counter(input())

if len(cnt) > 4:
    print(0)
else:
    for n in "345679":
        if n in cnt:
            print(0)
            break
    else:
        sorted_cnt = cnt.most_common()
        if len(sorted_cnt) == 4:
            if sorted_cnt[0][1] == sorted_cnt[-1][1]:
                print(8)
            else:
                print(2)
        else:
            print(1)
