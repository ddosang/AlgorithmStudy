N = int(input())
arr = [[0] * (n+2)]
for i in range(n):
    arr += [[0] + list(map(int, input().split())) + [0]]
arr += [[0] *  (n+2)]

count = 0
# for i in range(1, N+1):
#    for j in range(1, N+1):
#         if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i][j+1]:
#             count += 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if arr[i][j] <= arr[i + di][j + dj]:
                break
        else:
            cnt += 1

print(count)
