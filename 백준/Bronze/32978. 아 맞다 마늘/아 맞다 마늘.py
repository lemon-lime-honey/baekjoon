n = int(input())

ingredients = set(input().split())
used = set(input().split())

print(*ingredients.difference(used))
