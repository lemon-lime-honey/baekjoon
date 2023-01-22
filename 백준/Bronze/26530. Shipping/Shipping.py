n = int(input())

for i in range(n):
    x = int(input())
    total = 0
    for j in range(x):
        name, quantity, unit_price = map(str, input().split())
        quantity = int(quantity)
        unit_price = float(unit_price)
        
        total += quantity * unit_price
    print(f'${total:.2f}')