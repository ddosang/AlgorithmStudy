import sys
from collections import deque

def BFS(i, j):
    q = deque()
    q.append((i, j))
    town[i][j] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in adj:
            nx = x + dx
            ny = y + dy

            if not 0 <= nx < h:
                continue
            if not 0 <= ny < w:
                continue

            if town[nx][ny] == 1:
                q.append((nx, ny))
                town[nx][ny] = 0


adj = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1),  (-1, 1)]

w = 1
h = 1
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 or h == 0:
        break
    town = [[int(c) for c in sys.stdin.readline().split()] for _ in range(h)]

    sol = 0


    for i in range(h):
        for j in range(w):
            if town[i][j] == 1:
                BFS(i, j)
                sol += 1

    print(sol)
