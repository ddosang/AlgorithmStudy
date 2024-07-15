from collections import deque

def DFS(x, y):
    global cnt

    if (x, y) == end:
        cnt += 1
        return
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newX, newY = x + dx, y + dy
        if 0 <= newX < N and 0 <= newY < N and (not visited[newX][newY]) and arr[newX][newY] > arr[x][y]:
            visited[newX][newY] = 1
            DFS(newX, newY)
            visited[newX][newY] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_height = 10e8
max_height = 0
start = (0, 0)
end = (0, 0)

for i in range(N):
    for j in range(N):
        if min_height > arr[i][j]:
            min_height = arr[i][j]
            start = (i, j)
        if max_height < arr[i][j]:
            max_height = arr[i][j]
            end = (i, j)

cnt = 0
visited[start[0]][start[1]] = 1
DFS(start[0], start[1])
print(cnt)
