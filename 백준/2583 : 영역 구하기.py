import sys
from collections import deque
readl = sys.stdin.readline

def BFS(i, j):
    q = deque([(i, j)])
    board[i][j] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny, ncnt = x + dx, y + dy, cnt + 1

            if not 0 <= nx < M:
                continue
            if not 0 <= ny < N:
                continue

            if board[nx][ny] == 1:
                continue

            board[nx][ny] = 1
            q.append((nx, ny))
            cnt += 1

    return cnt



M, N, K = map(int, readl().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    sc, sr, ec, er = map(int, readl().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            board[i][j] = 1

# for i in range(M):
#     print(board[i])

cnt = []
            
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            cnt.append(BFS(i, j))



print(len(cnt))
print(*sorted(cnt))

