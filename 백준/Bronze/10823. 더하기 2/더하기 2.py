s = list()

while True:
    try:
        ipt = input()
        if not ipt:
            break
        s.append(ipt)
    except:
        break

nums = list(map(int, "".join(s).split(",")))
print(sum(nums))