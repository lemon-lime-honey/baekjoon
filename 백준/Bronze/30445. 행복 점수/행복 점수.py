import decimal


def _round(num):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return decimal.Decimal(num).quantize(decimal.Decimal('0.01'))


ipt = input()
h, g = 0, 0

for letter in ipt:
    if letter in "HAPPY":
        h += 1
    if letter in "SAD":
        g += 1

if h == g == 0:
    print(f"{50:.2f}")
else:
    result = h * 100 / (h + g)
    print(f"{_round(result):.2f}")
