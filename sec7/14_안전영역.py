from collections import deque
import sys
sys.setrecursionlimit(10**6) # DFS 로 하려면 추가해야함.

def BFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0 and arr[newX][newY] > rain:
                q.append((newX, newY))
                visited[newX][newY] = 1

def DFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < N and 0 <= newY < N and visited[newX][newY] == 0 and arr[newX][newY] > rain:
            visited[newX][newY] = 1
            DFS(newX, newY)
                


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = set()
for i in range(N):
    for j in range(N):
        arr2.add(arr[i][j])
arr2.add(0) # 아예 잠기지 않는 경우 고려해야함.

max_cnt = 0

# 비가 얼만큼 올지는 모르니까 있는 높이만큼 다 해보기
# 56 59 60 이렇게 있으면 비가 56 오나 57 오나 58 오나 56만 잠기는 케이스니까,
# arr 안에 있는 높이로 섬의 개수를 체크하고,
# 그 중 가장 큰 것을 저장해두면 됨.
for rain in arr2: 
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > rain:
                cnt += 1
                # BFS(i, j)
                DFS(i, j)
    
    max_cnt = max(cnt, max_cnt)

print(max_cnt)

visited = [[0] * N for _ in range(N)]
