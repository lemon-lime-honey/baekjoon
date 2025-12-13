n, m = map(int, input().split())
order = list()

for i in range(n):
    ipt = input().split()
    
    match ipt[0]:
        case "order":
            order.append((int(ipt[1]), int(ipt[2])))
        case "sort":
            order.sort(key=lambda x: (x[1], x[0]))
        case "complete":
            target = -1
            for idx, data in enumerate(order):
                if data[0] == int(ipt[1]):
                    target = idx
                    break
            del order[target]
            
    if order:
        print(*[x[0] for x in order])
    else:
        print("sleep")