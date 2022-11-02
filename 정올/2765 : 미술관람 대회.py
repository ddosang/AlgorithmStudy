import sys
from collections import deque
import copy

def BFS(picture, i, j, color):
    q = deque()
    q.append((i, j, color))
    picture[i][j] = 0

    while q:
        x, y, tcolor = q.popleft()

        for dx, dy in adj:
            nx = x + dx
            ny = y + dy

            if not 0 <= nx < N:
                continue
            if not 0 <= ny < N:
                continue

            if picture[nx][ny] != tcolor:
                continue

            q.append((nx, ny, picture[nx][ny]))
            picture[nx][ny] = 0




readl = sys.stdin.readline
N = int(readl())
picture = [[c for c in readl().strip()] for _ in range(N)]
copy = copy.deepcopy(picture)

adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt = 0
rgcnt = 0

for i in range(N):
    for j in range(N):
        if picture[i][j] != 0:
            BFS(picture, i, j, picture[i][j])
            cnt += 1

print(cnt)


for i in range(N):
    for j in range(N):
        if copy[i][j] == 'G':
            copy[i][j] = 'R'

cnt = 0
for i in range(N):
    for j in range(N):
        if copy[i][j] != 0:
            BFS(copy, i, j, copy[i][j])
            cnt += 1

print(cnt)
