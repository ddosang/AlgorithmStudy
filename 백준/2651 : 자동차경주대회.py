import sys
from collections import deque
import math
readl = sys.stdin.readline

def BFS():
    q = deque([(0, 0, 0)])
    time[0] = 0

    while q:
        x, cnt, t = q.popleft()

        # 지금 방문한 점보다 뒤에 있는 정비소를 전부 방문해본다.
        for nx in range(x + 1, N + 2):
            # dist 보다 큰건 방문 불가능. 다음꺼로 넘어갈 필요도 X
            if sum(dist[x + 1 : nx + 1]) > L:
                break

            ncnt = cnt + 1
            nt = t + time[nx]
            
            if nt >= visited[nx][1]:
                continue

            
            where[nx] = x
            visited[nx] = (ncnt, nt)
            q.append((nx, ncnt, nt))
            # print(nx, nt)

    return visited[-1]                



L = int(readl()) # 정비 받지 않고 가는 최대 거리
N = int(readl()) # 정비소의 개수
dist = [0] + list(map(int, readl().split())) # 인접한 정비소 사이 거리
time = [0] + list(map(int, readl().split())) + [0]


# 개수, 시간 순으로 표시
visited = [(N + 3, math.inf)] * (N + 2)
where = [0] * (N + 2)

cnt, totalTime = BFS()
print(totalTime)

if totalTime != 0:
    print(cnt - 1)

    sol = []
    i = where[N + 1]
    while i > 0:
        sol.append(i)
        i = where[i]

    print(*sol[::-1])