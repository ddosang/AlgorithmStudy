# 풀이
# 이거 항상 그냥 배열 인덱스 번호 규칙으로 풀었는데
# BFS 로 정중앙에서 N // 2 번만에 방문 가능한 곳만 방문하면 되는거였다니...
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append((N // 2, N // 2, 0))
res = arr[N//2][N//2]
visited = [[False] * N for _ in range(N)]
visited[N//2][N//2] = True

while q:
    x, y, level = q.popleft()

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx < N and 0 <= y + dy < N and (not visited[x+dx][y+dy]) and level < N // 2:
            q.append((x + dx, y + dy, level + 1))
            visited[x+dx][y+dy] = True
            res += arr[x+dx][y+dy]

print(res)
