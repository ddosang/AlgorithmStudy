# 내가 푼 것
# DFS 로 피잣집 고르고 BFS 로 피자집과 집 사이의 거리 탐방
# 2번 케이스에서 바로 시간초과
from collections import deque

def DFS(level, start):
    global min_dist

    if level == M:
        dis = BFS()
        min_dist = min(min_dist, dis)
        return
    
    for i in range(start, len(pizza)):
        if chk[i] != 1:
            chk[i] = 1
            res[level] = i
            DFS(level + 1, start + 1) # 여기가문제였다니
            chk[i] = 0


def BFS():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dist = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    q = deque()
    for i in res:
        x, y = pizza[i]
        q.append((x, y))
        visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0:
                q.append((newX, newY))
                visited[newX][newY] = 1
                dist[newX][newY] = dist[x][y] + 1

    result = 0
    for x, y in home:
        result += dist[x][y]
    return result



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
home = []
pizza = []
min_dist = 2 * N ** 3

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            pizza.append((i, j))

chk = [0] * len(pizza)
res = [0] * M


DFS(0, 0)
print(min_dist)


# 강의 코드
from collections import deque

def DFS(level, start):
    global min_dist

    if level == M:
        min_dist = min(min_dist, dist())
        return
    
    for i in range(start, len(pizza)):
        res[level] = i
        DFS(level + 1, i + 1) # 여기가 문제였음.. start+1 이 아니ㅏㄹ i+ 1

def dist():
    total = 0
    for hx, hy in home:
        min_dis = 2 * N
        for i in res:
            px, py = pizza[i]
            dis = abs(hx - px) + abs(hy - py)
            min_dis = min(min_dis, dis)
        total += min_dis
    
    return total

    


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
home = []
pizza = []
min_dist = 2 * N ** 3

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            pizza.append((i, j))

chk = [0] * len(pizza)
res = [0] * M


DFS(0, 0)
print(min_dist)
