n = int(input())
arr = [int(input()) for _ in range(n)]

local_min = 10000001

for i in range(n):
    local_min = 10000001
    for j in range(i + 1, n):
        if local_min > arr[j]:
            local_min = arr[j]
            local_min_index = j

    if local_min < arr[i]:
        temp = arr[i]
        arr[i] = arr[local_min_index]
        arr[local_min_index] = temp

    print(arr)

for i in range(n):
    print(arr[i])
