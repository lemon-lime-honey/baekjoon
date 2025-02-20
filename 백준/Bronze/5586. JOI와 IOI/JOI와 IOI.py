ipt = input()

idx, joi, ioi = 0, 0, 0

while idx < len(ipt) - 2:
    match ipt[idx : idx + 3]:
        case "JOI":
            joi += 1
        case "IOI":
            ioi += 1
    idx += 1

print(joi)
print(ioi)
