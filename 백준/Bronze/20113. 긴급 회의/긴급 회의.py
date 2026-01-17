from collections import Counter

n = int(input())
vote = Counter(map(int, input().split())).most_common()

if vote[0][0] == 0:
    vote = vote[1:]

if len(vote) != 1 and vote[0][1] == vote[1][1]:
    print("skipped")
else:
    print(vote[0][0])
