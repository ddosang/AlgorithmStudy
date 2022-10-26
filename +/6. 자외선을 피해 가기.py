import sys
from collections import deque


def BFS():
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    q = deque()
    q.append((0, 0, sun_map[0][0]))
    min_sun_map[0][0] = sun_map[0][0]

    while q:
        r, c, sun = q.popleft()

        # 여기서는 BFS 가 무조건 작은 것을 선택하면서 가는게 아니라 모든 경로에 대해 탐색해보고 가장 작은 값을 선택해야해서 종료 조건은 안걸어주는 것이 맞다.
#        if r == N - 1 and c == N - 1:
#            return sun

        for x, y in moves:
            tr, tc = r + x, c + y

            if not 0 <= tr < N:
                continue
            if not 0 <= tc < N:
                continue

            tsun = sun + sun_map[tr][tc]

            if min_sun_map[tr][tc] <= tsun:
                continue

            min_sun_map[tr][tc] = tsun
            q.append((tr, tc, tsun))
    return -1



N = int(sys.stdin.readline())

sun_map = []
for i in range(N):
    l = []
    for c in sys.stdin.readline()[:-1]:
        l += [int(c)]
    sun_map += [l]

# min_sun_map = [[999999] * N] * N
min_sun_map = [[999999] * N for _ in range(N)]

BFS()
print(min_sun_map[N - 1][N - 1])
