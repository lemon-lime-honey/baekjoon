import sys
input = sys.stdin.readline

n = int(input())
maximum = [0, 0, 0]
minimum = [0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().split())
    maximum = [a + max(maximum[0], maximum[1]), b + max(maximum[0], maximum[1], maximum[2]), c + max(maximum[1], maximum[2])]
    minimum = [a + min(minimum[0], minimum[1]), b + min(minimum[0], minimum[1], minimum[2]), c + min(minimum[1], minimum[2])]

print(max(maximum), min(minimum))