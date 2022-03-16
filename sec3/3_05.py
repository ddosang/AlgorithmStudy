n, m = map(int, input().split())

arr = list(map(int, input().split()))

lt = 0
rt = 1
count = 0
sum_arr = arr[lt]

while rt <= n:
    sum_arr = sum(arr[lt:rt])
    if sum_arr == m:
        count += 1
        lt += 1
    elif sum_arr > m:
        lt += 1
    else:
        rt += 1

print(count)
