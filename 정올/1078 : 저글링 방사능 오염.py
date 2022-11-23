import sys
from collections import deque
readl = sys.stdin.readline

def BFS(i, j):
    q = deque([(i, j, 3)])
    smap[i][j] = 0

    while q:
        x, y, time = q.popleft()
        
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny, ntime = x + dx, y + dy, time + 1

            if not 0 <= nx < h:
                continue
            if not 0 <= ny < w:
                continue

            if smap[nx][ny] == 0:
                continue
            
            q.append((nx, ny, ntime))
            smap[nx][ny] = 0
    
    return ntime - 1

            
    

w, h = map(int, readl().split())
smap = [[int(c) for c in readl().rstrip()] for _ in range(h)]
x, y = map(int, readl().split())

print(BFS(y - 1, x - 1))

live = 0
for i in range(h):
    live += smap[i].count(1)
print(live)