import sys
from collections import deque

# 입력
w, h = map(int, sys.stdin.readline().split())
startW, startH, endW, endH = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline())[:-1] for _ in range(h)]

queue = deque()

# 우측 하단으로 이동한다는 규칙을 세우면 안됨 -> 당장은 좋을 수도 있으나 돌아가는 길일수도.
# 목적지까지 갈 수 있는 모든 경로를 다 시도해보자! -> BFS
# 상태(로봇의 위치), 해당 상태가 어떻게 발전할 것인지(상하좌우 갈 수 있는 곳으로 이동)를 염두에 두고 코드를 짜야함.

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

move = [up, down, left, right]

queue.append((startH - 1, startW - 1, 0))
maze[startH - 1][startW - 1] = 1

while queue:
    th, tw, time = queue.popleft()

    if nw == endW - 1 and nh == endH - 1:
        print(time)
        break

    for ph, pw in move:
        nh, nw, ntime = th + ph, tw + pw, time + 1
        # if nw < 0 or w <= nw or nh < 0 or h <= nh: # 미로 밖으로 벗어남
        #     continue

        if not 0 <= nw < w:
            continue

        if not 0 <= nh < h:
            continue
        
        # 여기서 걸러져야 하는 것이 안걸러진체로 queue 에 들어가있는 경우가 있음... 왤까?
        if maze[nh][nw] == 1: # 벽
            continue


        # 만약 BFS 에서 뻗은 것에서 목적지가 같다면 굳이 큐에 넣을 필요가 없음.
        queue.append((nh, nw, ntime))
        maze[nh][nw] = 1
