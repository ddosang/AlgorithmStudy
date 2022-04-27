first = input()
second = input()

ana_dict = {}

for c in first:
    if c in ana_dict.keys():
        ana_dict[c] += 1
    else:
        ana_dict[c] = 1

for c in second:
    if c in ana_dict.keys():
        ana_dict[c] -= 1

for key in ana_dict.keys():
    if ana_dict[key] != 0:
        print("NO")
        break
else:
    print("YES")
