import sys
from collections import deque

readl = sys.stdin.readline

def BFS(i, j):
    q = deque([(i, j)])
    ch[i][j] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy

            if not 0 <= nx <= n + 1:
                continue
            if not 0 <= ny <= n + 1:
                continue

            if 도화지[nx][ny] == 1:
                ch[nx][ny] = 1
                cnt += 1
                continue

            if ch[nx][ny] == 1:
                continue


            ch[nx][ny] = 1
            q.append((nx, ny))

    return cnt




n = 100

도화지 = [[0] * (n + 2) for _ in range(n + 2)]
ch = [[0] * (n + 2) for _ in range(n + 2)]

# 입력
m = int(readl())
for _ in range(m):
    sx, sy = map(int, readl().split())
    for i in range(sx, sx + 10):
        for j in range(sy, sy + 10):
            도화지[i][j] = 1

sol = 0
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0 and 도화지[i][j] == 0:
            sol += BFS(i, j)

print(sol)
