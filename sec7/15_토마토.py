# 풀이
from collections import deque

# level 을 하나씩만 도는 BFS
def BFS():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    
    # level 을 하나씩 돌려면 이번 레벨에서 큐에 넣은 만큼 돌면 됨.
    for _ in range(len(q)):
        x, y = q.popleft()

        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]

            if 0 <= newX < M and 0 <= newY < N and arr[newX][newY] == 0:
                q.append((newX, newY))
                arr[newX][newY] = 1
                cnt += 1
    
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
q = deque()

tomato = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            tomato += 1
        elif arr[i][j] == 1:
            q.append((i, j))

while True:
    changed = BFS()
    tomato -= changed

    if changed == 0:
        break

    cnt += 1

print(cnt if tomato == 0 else -1)



# 강의 코드
from collections import deque
import copy

def BFS():
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    tomato = 0

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                tomato += 1
            elif arr[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]

            if 0 <= newX < M and 0 <= newY < N and arr[newX][newY] == 0:
                q.append((newX, newY))
                arr[newX][newY] = 1
                dist[newX][newY] = dist[x][y] + 1 # BFS 를 도는데 각 칸에 가는 거리를 저장해놨다가


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dist = [[0] * N for _ in range(M)]


BFS()

tomato = 0
res = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            tomato += 1
        if dist[i][j] > res:
            res = dist[i][j] # BFS 돌고 나서 dist 최댓값 사용.
          
print(res if tomato == 0 else -1)
