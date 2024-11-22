h = int(input())
m = int(input())

hour = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "one",
]
minute = [
    " o' clock",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "quarter",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "half",
]

if m == 0:
    print(f"{hour[h]} o' clock")
elif m == 1:
    print(f"{minute[m]} minute past {hour[h]}")
elif m in (15, 30):
    print(f"{minute[m]} past {hour[h]}")
elif m < 30:
    print(f"{minute[m]} minutes past {hour[h]}")
elif m == 59:
    print(f"{minute[60 - m]} minute to {hour[h + 1]}")
elif m == 45:
    print(f"{minute[60 - m]} to {hour[h + 1]}")
else:
    print(f"{minute[60 - m]} minutes to {hour[h + 1]}")