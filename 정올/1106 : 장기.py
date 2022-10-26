import sys
from collections import deque

def BFS(N, M, R, C, S, K):

    # 이동 가능한 방향 8가지 (x, y 그래프로 보는거랑 행렬로 생각했을 때랑 축의 위치도 반대고 x, y 쌍 위치도 반대임!)
    move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    q = deque()

    q.append((R, C, 0))
    board[R][C] = 1

    while q:
        r, c, cnt = q.popleft()

        if r == S and c == K:
            return cnt

        for x, y in move:
            tr, tc, tcnt = r + x, c + y, cnt + 1

            if not 1 <= tr <= N:
                continue
            if not 1 <= tc <= M:
                continue

            # 같은 것도 포함.
            if (tcnt >= board[tr][tc]):
                continue

            q.append((tr, tc, tcnt))
            board[tr][tc] = tcnt

    return -1
