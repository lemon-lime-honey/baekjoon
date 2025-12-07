k = input()

if len(k) > 1:
    gap = -1
    flag = False

    for i in range(len(k) - 1):
        if not flag:
            gap = int(k[i + 1]) - int(k[i])
            flag = True
        elif int(k[i + 1]) - int(k[i]) != gap:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
