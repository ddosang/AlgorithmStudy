import sys
from collections import deque

readl = sys.stdin.readline

def BFS():
    global happy

    q = deque()

    sx, sy = positions[0]
    q.append((sx, sy))
    visited[0] = 1

    while q:
        x, y = q.popleft()

        # 마지막 장소에서 곧장 페스티벌에 갈 수 있다면 happy
        if abs(positions[n + 1][0] - x) + abs(positions[n + 1][1] - y) <= 1000:
            happy = 1
            return

        # 페스티벌에 바로 갈 수 없다면 가까운 편의점에 들름.
        for i in range(1, n+1):
            if not visited[i]:
                nx, ny = positions[i]
                dist = abs(nx - x) + abs(ny - y)
                if dist <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1


t = int(readl())
for _ in range(t):
    n = int(readl()) # 편의점 개수
    positions = [list(map(int, readl().split())) for _ in range(n + 2)]

    visited = [0] * (n + 2)
    happy = 0
    BFS()

    print("happy" if happy else "sad")
