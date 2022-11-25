import sys
from collections import deque
readl = sys.stdin.readline

def BFS(i, j, mid):
    q = deque([(i, j)])
    ch[i][j] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        if cnt >= 최소방문개수:
            return cnt
        
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy

            if not 0 <= nx < N or not 0 <= ny < N or ch[nx][ny] == 1:
                continue

            strength = abs(farm[nx][ny] - farm[x][y])

            if strength > mid:
                continue

            q.append((nx, ny))
            ch[nx][ny] = 1
            cnt += 1

    return cnt



N = int(readl())
farm = [list(map(int, readl().split())) for _ in range(N)]

최소방문개수 = (N * N + 1) // 2

# print(BFS(0, 0, 1))

# 트랙터의 힘이 mid 일 때,
# 농장의 모든 곳에서 시작해서 몇 개까지 갈 수 있는지 알아본다.
# 그게 반보다 더 많으면 d 를 크게 만들어야하고
# 반보다 더 작으면 d 를 작게 만들어야 함.
max_farm = 0
min_farm = 1000001
for i in range(N):
    for j in range(N):
        if farm[i][j] > max_farm:
            max_farm = farm[i][j]
        if farm[i][j] < min_farm:
            min_farm = farm[i][j]


sol = -1
left = 0
right = max_farm - min_farm

while left <= right:
    mid = (left + right) // 2

    check = 0
    # 이걸 왜 안에 넣어야할까?
    # BFS 에서 해당 지점에서 전부 가는게 아니라 한번 가본 점은 안보고 넘어감.
    # 한번 가본 점 : 어차피 거기로 가서 다시 퍼져봤자 걔 주변에 거리차가 d 보다 큰게 있어서 cnt 가 작게 나올것임. 우린 max 만 구하면 되는데! -> 그래서 빼도 됨.
    ch = [[0] * N for _ in range(N)]
    breaked = False
    for i in range(N):
        for j in range(N):
            # 이런 미친.. ch 배열 안으로 넣고 위에처럼 이유까지 찾아놓고...
            # 이 줄 안넣어서 계속 시간초과남 ㅡㅡ
            if ch[i][j] == 1: continue
            check = max(check, BFS(i, j, mid))
            if check >= 최소방문개수:
                breaked = True
                break
        if breaked:
            break
    
    if breaked:
        right = mid - 1
        sol = mid
    else:
        left = mid + 1

print(sol)