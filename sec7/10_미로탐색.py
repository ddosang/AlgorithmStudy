# 풀이
from collections import deque

def DFS(x, y, dist):
    global cnt
    # print(x, y)

    if x == 6 and y == 6:
        cnt += 1
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x + dx < 0 or 6 < x + dx or y + dy < 0 or 6 < y + dy:
            continue
    
        if arr[x + dx][y + dy] == 1:
            continue

        arr[x + dx][y + dy] = 1
        DFS(x + dx, y + dy, dist + 1)
        arr[x + dx][y + dy] = 0


arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
arr[0][0] = 1
DFS(0, 0, 0)
print(cnt)
