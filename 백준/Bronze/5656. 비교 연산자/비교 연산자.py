import sys

input = sys.stdin.readline

idx = 1

while True:
    ipt = list(input().split())

    if ipt[1] == "E":
        break

    match ipt[1]:
        case ">":
            if int(ipt[0]) > int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
        case ">=":
            if int(ipt[0]) >= int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
        case "<":
            if int(ipt[0]) < int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
        case "<=":
            if int(ipt[0]) <= int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
        case "==":
            if int(ipt[0]) == int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
        case "!=":
            if int(ipt[0]) != int(ipt[2]):
                print(f"Case {idx}: true")
            else:
                print(f"Case {idx}: false")
    idx += 1
