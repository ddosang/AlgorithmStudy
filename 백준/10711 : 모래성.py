import sys
from collections import deque
readl = sys.stdin.readline

# 성이 있는 격자 주변 8방향에 성이 없는 격자의 개수가 성의 강도보다 크거나 같으면 붕괴.

def BFS():
    global castle_cnt

    q = deque()

    # 모래를 기준으로 탐색.
    for i in range(h):
        for j in range(w):
            if sand[i][j] == 0:
                q.append((i, j))

    time = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
                nx, ny = x + dx, y + dy

                # 가생이 제거
                if not 0 <= nx < h:
                    continue
                if not 0 <= ny < w:
                    continue
                
                # 모래는 신경쓸 필요 없음.
                if sand[nx][ny] == 0:
                    continue

                # 모래 근처에 있는 성이면 -1
                sand[nx][ny] -= 1

                # 만약에 여전히 성이 남아있으면 신경쓸 필요 X
                if sand[nx][ny] != 0:
                    continue

                # 성이 모래가 되는 순간 큐에 넣으면 됨.
                # ch[nx][ny] = ch[x][y] + 1
                # cnt = max(cnt, ch[nx][ny])
                q.append((nx, ny))

        time += 1

    return time - 1


h, w = map(int, readl().split())
sand = [[int(c) if c.isdigit() else 0 for c in readl().rstrip()] for _ in range(h)]

ch = [[0] * w for _ in range(h)]


print(BFS())