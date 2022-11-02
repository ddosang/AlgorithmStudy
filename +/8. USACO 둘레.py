import sys
from collections import deque

def BFS(i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    들판[i][j] = 2

    while q:
        x, y = q.popleft()

        for dx, dy in adj:
            nx = x + dx
            ny = y + dy

            if not 0 <= nx < 102:
                continue
            if not 0 <= ny < 102:
                continue

            if 들판[nx][ny] == 0:
                q.append((nx, ny))
                들판[nx][ny] = 2 # 빈 곳을 탐색해야하니까 2로 표시.
            elif 들판[nx][ny] == 1:
                cnt += 1 # 주변에 건초가 있으면 1을 늘린다. (해당 뱡향으로 edge 가 생기는 것!)
                # hole 은 애초에 세어지지도 않음.
    return cnt


readl = sys.stdin.readline

n = int(readl())
# 맨 가장자리가 건초여도 edge 를 세어줘야하기 때문에 padding 추가
건초들 = [list(map(int, readl().split())) for _ in range(n)]

들판 = [[0] * 102 for _ in range(102)]
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for x, y in 건초들:
    들판[y][x] = 1

    # 건초가 있는 주변만 빈 자리를 따지면 됨.



print(BFS(0, 0))
