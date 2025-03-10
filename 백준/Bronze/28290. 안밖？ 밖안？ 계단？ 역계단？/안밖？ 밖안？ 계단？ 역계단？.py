types = {"in-out": {"fdsajkl;", "jkl;fdsa"},
         "out-in": {"asdf;lkj", ";lkjasdf"},
         "stairs": {"asdfjkl;"},
         "reverse": {";lkjfdsa"}}

s = input()

for key, value in types.items():
    if s in value:
        print(key)
        break
else:
    print("molu")
