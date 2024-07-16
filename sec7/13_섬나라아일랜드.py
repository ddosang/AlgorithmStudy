from collections import deque

def BFS(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    q = deque()
    q.append((x, y))
    arr[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(8):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] == 1:
                q.append((newX, newY))
                arr[newX][newY] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            BFS(i, j)

print(cnt)
