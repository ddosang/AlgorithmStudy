import sys
from collections import deque
readl = sys.stdin.readline

# 정육면체라 탐색 지점이 6개로 늘어났을 뿐,
# BFS 로 똑같이 탐색하면 된다.
def BFS():
    # ch = [[[0] * C for _ in range(R)] for _ in range(L)]
    q = deque()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if cube[i][j][k] == 'S':
                    q.append((i, j, k, 0))
                    cube[i][j][k] = '#'
                    break


    while q:
        x, y, z, time = q.popleft()
        # 상하좌우앞뒤
        for dx, dy, dz in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nx, ny, nz = x + dx, y + dy, z + dz
            ntime = time + 1

            # 범위 검사.
            if (not 0 <= nx < L) or (not 0 <= ny < R) or (not 0 <= nz < C):
                continue

            if cube[nx][ny][nz] == 'E':
                return ntime

            # 벽
            if cube[nx][ny][nz] == '#':
                continue

            cube[nx][ny][nz] = '#'
            q.append((nx, ny, nz, ntime))
    
    return -1




L, R, C = map(int, readl().split())

while (L, R, C) != (0, 0, 0):
    cube = []
    for _ in range(L):
        면 = [list(readl().strip()) for _ in range(R)]
        cube.append(면)
        readl()
        
    # cube print
    # for i in range(L):
    #     for j in range(R):
    #         print(cube[i][j])
    #     print()
    
    b = BFS()
    if b != -1:
        print("Escaped in " + str(b) + " minute(s).")
    else:
        print("Trapped!")


    
    L, R, C = map(int, readl().split())
    