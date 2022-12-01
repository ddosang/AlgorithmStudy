import sys
from collections import deque
readl = sys.stdin.readline

# BFS 로 방문하면서 각 상점에 대한 거리 min_dist 를 채움.
def BFS(i, j):
    global N

    q = deque([(i, j, 0)])
    board[i][j] = -1 # 방문 체크 -1 로.

    while q:
        x, y, time = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny, ntime = x + dx, y + dy, time + 1
            # 입력 범위 체크
            if not 0 <= nx <= H or not 0 <= ny <= W:
                continue
            # 벽이거나 방문
            if board[nx][ny] == 200 or board[nx][ny] == -1:
                continue
                
            if board[nx][ny] != 0:
                min_dist[board[nx][ny]] = min(min_dist[board[nx][ny]], ntime)

                # 시간을 조금 줄이기 위해서 추가
                N -= 1
                if N == 0:
                    return

            board[nx][ny] = -1
            q.append((nx, ny, ntime))
            

 
W, H = map(int, readl().split())
N = int(readl())

# 200 은 벽. - 가장자리만 방문 가능하니 안쪽을 벽으로 채움.
board = [[0] + [200] * (W - 1) + [0] if 1 <= i <= H - 1 else [0] * (W + 1)  for i in range(H + 1)]
person = (-1, -1)
min_dist = [300] * (N + 1)

# 각 상점이 있는 자리를 x, y 좌표로 바꾸고 보드에 상점 번호로 표시.
for i in range(N + 1):
    dir, pos = map(int, readl().split())

    (x, y) = (-1, -1)
    if dir == 1: # 북
        (x, y) = (0, pos)
    elif dir == 2: # 남
        (x, y) = (H, pos)
    elif dir == 3: # 서
        (x, y) = (pos, 0)
    elif dir == 4:
        (x, y) = (pos, W)

    if i == N:
        person = (x, y)
        break

    board[x][y] = i + 1

x, y = person
BFS(x, y)
print(sum(min_dist[1:]))