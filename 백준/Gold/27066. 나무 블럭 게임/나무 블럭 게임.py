import sys

input = sys.stdin.readline

n = int(input())
blocks = list(map(int, input().split()))
total = sum(blocks)

blocks.sort()

print(max(total / n, blocks[n - 2]))