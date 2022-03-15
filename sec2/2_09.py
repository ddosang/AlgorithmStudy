n = int(input())
prizes = []

for i in range(n):
    arr = list(map(int, input().split()))
    diff_arr = sorted(list(set(arr)), reverse=True)


    if len(diff_arr) == 1:
        prizes.append(10000 + diff_arr[0] * 1000)
    elif len(diff_arr) == 2:
        prizes.append(1000 + diff_arr[0] * 100)
    else:
        prizes.append(diff_arr[0] * 100)

print(max(prizes))
