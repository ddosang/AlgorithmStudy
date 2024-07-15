# 1. BFS
from collections import deque

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            newX, newY = x + dx, y + dy

            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0 and arr[newX][newY] == 1:
                q.append((newX, newY))
                visited[newX][newY] = 1
                cnt += 1

    return cnt

N = int(input())
arr = [[int(x) for x in list(input())] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnts = []

# print(arr)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = BFS(i, j)
            cnts.append(cnt)

cnts.sort()
print(len(cnts))
print(*cnts, sep='\n')


# 2. DFS
def DFS(x, y):
    global cnt
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        newX, newY = x + dx, y + dy

        if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] == 1 and visited[newX][newY] == 0:
            visited[newX][newY] = 1
            DFS(newX, newY)
            cnt += 1

N = int(input())
arr = [[int(x) for x in list(input())] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnts = []

# print(arr)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            DFS(i, j)
            cnts.append(cnt)

cnts.sort()
print(len(cnts))
print(*cnts, sep='\n')
