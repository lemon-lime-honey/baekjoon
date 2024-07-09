def solve(start, end, reverse):
    global result
    if result or start < 0 or end >= len(t) or end < start:
        return
    if (
        not reverse
        and t[start : end + 1] == s
        or reverse
        and t[start : end + 1] == s[::-1]
    ):
        result = True
    if not reverse:
        if t[start] == "B":
            solve(start + 1, end, True)
        if t[end] == "A":
            solve(start, end - 1, False)
    else:
        if t[start] == "A":
            solve(start + 1, end, True)
        if t[end] == "B":
            solve(start, end - 1, False)


s = input()
t = input()
result = False
solve(0, len(t) - 1, False)
print(1 if result else 0)
