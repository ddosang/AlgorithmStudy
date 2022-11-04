import sys
from collections import deque
import copy

readl = sys.stdin.readline


def BFS(cheese_map, i, j):
    q = deque()
    q.append((i, j))
    # 치즈 한번 없애고 다음에 또 새로 방문해야하니까 여기서 ch 만들어준다.
    ch = [[0] * w for _ in range(h)]

    while q:
        x, y = q.popleft()
        ch[i][j] = 1
        # print(x, y)

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하좌우
            nx = x + dx
            ny = y + dy

            if not 0 <= nx < h:
                continue
            if not 0 <= ny < w:
                continue

            # 이미 방문함.
            if ch[nx][ny] == 1:
                continue

            # 녹아서 없어짐
            # 대신 녹아서 없어진 것에 또 방문하면 안되므로 ch 로 방문 체크 해야함.
            if cheese_map[nx][ny] == 1:
                cheese_map[nx][ny] -= 1
                ch[nx][ny] = 1
                continue

            # 0 (공기) 이면서 방문 안한것만 방문할 수 있게 됨.
            ch[nx][ny] = 1
            q.append((nx, ny))


h, w = map(int, readl().split())
cheese_map = [list(map(int, readl().split())) for _ in range(h)]
copy_map = copy.deepcopy(cheese_map)

# 가장자리가 있으므로 0,0 은 구멍일수가 없음.
# 0, 0 에서 시작해서 주변에 치즈가 있으면 치즈를 없애주면 됨.
existCheese = True
time = 0
while existCheese:
    BFS(cheese_map, 0, 0)
    time += 1

    # 치즈가 하나라도 남아있으면 실행.
    for i in range(1, h - 1):
        if 1 in cheese_map[i]:
            existCheese = True
            break
    else:
        existCheese = False

print(time)

cheese_count = 0
# 치즈가 없어지기 바로 전단계까지 실행 후,
for _ in range(time - 1):
    BFS(copy_map, 0, 0)

# 치즈 개수 카운트
for i in range(1, h - 1):
    cheese_count += copy_map[i].count(1)

print(cheese_count)
