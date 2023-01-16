envelope, poster, pamphlet = map(int, input().split())

c4 = 2 * 0.229 * 0.324
a3 = 2 * 0.297 * 0.420
a4 = 0.210 * 0.297

print(c4 * envelope + a3 * poster + a4 * pamphlet)