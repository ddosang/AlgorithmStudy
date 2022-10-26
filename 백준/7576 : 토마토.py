import sys
from collections import deque


def BFS():
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우 에 영향.

    count = 0

    q = deque()

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                q.append((i, j, 1))
            elif tomatoes[i][j] == 0:
                count += 1

    if count == 0:
        return 0


    while q:
        r, c, day = q.popleft()

        for x, y in moves:
            tr, tc, tday = r + x, c + y, day + 1

            if not 0 <= tr < N:
                continue
            if not 0 <= tc < M:
                continue

            if tomatoes[tr][tc] != 0:
                continue

            q.append((tr, tc, tday))
            tomatoes[tr][tc] = tday
            count -= 1

            # 여기서 거를것.
            if count == 0:
                return day


    return -1
