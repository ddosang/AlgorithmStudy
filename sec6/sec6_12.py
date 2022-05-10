n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    start, end, dist = map(int, input().split())
    arr[start - 1][end - 1] = dist

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= ' ')
    print()
