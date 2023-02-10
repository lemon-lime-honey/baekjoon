t = int(input())

for i in range(t):
    item_dict = dict()
    n = int(input())
    result = 1

    for j in range(n):
        name, kind = map(str, input().split())

        if kind in item_dict:
            item_dict[kind] += 1
        else:
            item_dict[kind] = 1
    
    for num in item_dict.values():
        result *= (num + 1)
    
    print(result - 1)