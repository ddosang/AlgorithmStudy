n, m = map(int, input().split())

sum_dict = { x: 0 for x in range(2, n+m+1) }

for i in range(1, n+1):
    for j in range(1, m+1):
        sum_dict[i+j] += 1

max = max(sum_dict.values())

for key in sum_dict.keys():
    if sum_dict[key] == max:
        print(key, end=" ")
