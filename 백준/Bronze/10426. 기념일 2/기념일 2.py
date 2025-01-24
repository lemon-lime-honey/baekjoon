from datetime import datetime, timedelta

ipt = input().split()

start = datetime.strptime(ipt[0], "%Y-%m-%d")
end = start + timedelta(days=int(ipt[1]) - 1)

print(end.date())
