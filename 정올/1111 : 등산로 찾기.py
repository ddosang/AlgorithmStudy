import sys
from collections import deque
readl = sys.stdin.readline


def BFS():
    # strength 배열을 그냥 큰 값으로 넣고 시작했으면, 0 에서 시작하면 됨.
    q = deque([(0, 0, 0)])
    strength[0][0] = 0
    # q = deque()

    # strength 배열 가생이를 0으로 채워놓고 시작했으면, 0 인거 다 넣고 시작해야함!!!
    # for n in range(1, N+1):
    #     q.append((0, n, 0))
    #     q.append((N+1, n, 0))
    #     q.append((n, 0, 0))
    #     q.append((n, N+1, 0))

    while q:
        r, c, st = q.popleft() # 이전거에서 더해야하니까 배열 자체의 값을 갱신하지 말고, st 를 이용해서 갱신하자.

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc

            # 배열 범위 체크
            if not 0 <= nr < N + 2:
                continue
            if not 0 <= nc < N + 2:
                continue


            # 힘.
            nst = st + (mountain[r][c] - mountain[nr][nc] if mountain[nr]
                                   [nc] <= mountain[r][c] else (mountain[nr][nc] - mountain[r][c]) ** 2)

            # 목적지이면. -> 목적지까지 가는 가장 작은 길을 갱신해야하니
            # 탈출하면 안됨. 그냥 마지막에 배열 값으로 return
            # if (nr, nc) == (DR, DC):
            #     return st

            # 지금 온 길이 이미 방문한 것보다 힘이 더듬..
            if nst >= strength[nr][nc]:
                continue

            strength[nr][nc] = nst
            q.append((nr, nc, nst))

    return strength[DR][DC]


N = int(readl())
DR, DC = map(int, readl().split())
mountain = [[0] + list(map(int, readl().split())) + [0]
            if 1 <= i <= N else [0] * (N + 2) for i in range(N + 2)]
# strength = [[0] + [2501] * N + [0] if 1 <= i <= N else [0] * (N + 2) for i in range(N + 2)]
strength = [[2501] * (N + 2) for _ in range(N + 2)]

# for i in range(N + 2):
#     print(strength[i])



print(BFS())
