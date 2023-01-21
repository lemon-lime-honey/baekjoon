k = int(input())
commision = 25 + k * 0.01

if commision < 100:
    commision = 100
if commision > 2000:
    commision = 2000

print(f'{commision:.2f}')
