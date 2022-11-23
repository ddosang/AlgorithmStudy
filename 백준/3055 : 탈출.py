
import sys
from collections import deque
readl = sys.stdin.readline

def BFS():

    # 갈 수 있는 곳 : 빈 곳 . 화가 S
    # 갈 수 없는 곳 : 홍수 * 바위 X 방문 ,
    # 종료 조건 : 비버 D 
    q = deque()

    for i in range(R + 2):
        for j in range(C + 2):
            if bmap[i][j] == 'S':
                q.append((i, j))
                time[i][j] = 0
                bmap[i][j] = ','

            if bmap[i][j] == '*':
                floodq.append((i, j))

    cur = 0
    while q:
        # 홍수 먼저 * 로 채우고,
        for i in range(len(floodq)):
            x, y = floodq.popleft()

            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy

                # 방문 체크.
                # 이미 홍수가 났거나 벽이나 비버 집 -> 방문 X
                if bmap[nx][ny] == 'X' or bmap[nx][ny] == '*' or bmap[nx][ny] == 'D':
                    continue

                # * 로 만들고
                bmap[nx][ny] = '*'
                # 방금 홍수난 곳을 다음에 방문할 수 있게 큐에 넣는다.
                floodq.append((nx, ny))

                
        # for i in range(R + 2):
        #     print(bmap[i], ch[i])

        # 비버굴을 찾아서 이동!!
        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy

                # 홍수, 바위로는 갈 수 없음.
                if bmap[nx][ny] == '*' or bmap[nx][ny] == 'X':
                    continue

                # 이전에 거기 간 시간이 더 짧다면 갈 수 없음.
                if time[nx][ny] <= time[x][y] + 1:
                    continue
                
                # 비버 굴이면 시간 return
                if bmap[nx][ny] == 'D':
                    return time[x][y] + 1

                # 시간 갱신
                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny))

    return -1
    

T = int(readl())
for _ in range(T):
    R, C = map(int, readl().split())
    bmap = [['X'] + [c for c in readl().rstrip()] + ['X'] if 1 <= i <= R else ['X'] * (C + 2) for i in range(R + 2)]


    # 화가도 움직이고 홍수(지도 자체를 바꾸면 됨)도 움직임.
    floodq = deque()

    time = [[0] + [R * C + 1] * C + [0] if 1 <= i <= R else [0] * (C + 2) for i in range(R + 2)] # 화가 시간 체크

    b = BFS()
    print(b if b != -1 else "KAKTUS")