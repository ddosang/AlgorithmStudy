import sys
from collections import deque

readl = sys.stdin.readline

def BFS():
    q = deque([(1, 1)])
    지도[1][1] = 2 # 장애물은 1로 체크, 방문은 2로 체크

    cnt = 0

    i = 0

    while q:
        x, y = q.popleft()
        # print(x, y)
        dx, dy = move[방향[i % 4]]
        nx, ny = x + dx, y + dy

        if not 0 <= nx <= n + 1:
            continue
        if not 0 <= ny <= n + 1:
            continue

        # 가는 도중에 방문한 길을 만나면 거기서 끝
        if 지도[nx][ny] == 2:
            break

        # 장애물을 만나면 방향을 틀어야함.
        if 지도[nx][ny] == 1:
            # 한번 틀고,
            i += 1
            dx, dy = move[방향[i % 4]]

            # 갔던 길인지 체크
            if 지도[x + dx][y + dy] == 2:
                break

            # 벽이면 다시 틀어본다.
            breaked = False
            while 지도[x + dx][y + dy] == 1:
                i += 1
                dx, dy = move[방향[i % 4]]

                if 지도[x + dx][y + dy] == 2:
                    breaked = True
                    break

            if breaked:
                break


            # 가능하면 틀어진 방향을 큐에 넣는다.
            q.append((x + dx, y + dy))
            지도[x + dx][y + dy] = 2
            cnt += 1
            continue

        지도[nx][ny] = 2
        q.append((nx, ny))
        cnt += 1

    return cnt



n = int(readl())
지도 = [[1] + list(map(int, [c for c in readl().strip()])) + [1] if 1 <= i <= n else [1] * (n + 2) for i in range(n + 2)]
방향 = [i - 1 for i in list(map(int, readl().split()))]
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# ch = [[0] * (n + 2) for _ in range(n + 2)]

print(BFS())
