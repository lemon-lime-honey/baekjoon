import sys

exchange = {'kg': '2.2046lb', 'l': '0.2642g', 'lb': '0.4536kg', 'g': '3.7854l'}
t = int(sys.stdin.readline())

for i in range(t):
    amount, unit = map(str, sys.stdin.readline().strip().split())
    amount = float(amount)
    rate = float(exchange[unit][:6])
    print(f'{amount * rate:.4f} {exchange[unit][6:]}')