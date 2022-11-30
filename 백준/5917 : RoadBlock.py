import sys
from collections import deque
import math
readl = sys.stdin.readline

def init(roads):
    # 길은 양방향이니까 시작 - 끝 뒤집어서 저장.
    newRoads = roads + [[end, start, dist] for start, end, dist in roads]
    
    dict = {x[0]: [] for x in newRoads}
    for start, end, dist in newRoads:
        dict[start].append((end, dist))
    
    dists = [math.inf] * (N + 1)

    return dict, dists


def BFS():
    global dict, dists

    # 집은 1
    q = deque([(1, 0)])
    dists[1] = 0

    while q:
        x, dist = q.popleft()

        for nx, d in dict[x]:
            nd = dist + d

            if dists[nx] <= nd:
                continue

            dists[nx] = nd
            q.append((nx, nd))
            temppath[nx] = x

    # 목적지는 N
    return dists[N]

N, M = map(int, readl().split())
roads = [list(map(int, readl().split())) for _ in range(M)]

dict, dists = init(roads)
temppath = [0] * (N + 1)

# 길을 바꾸지 않았을 때 최단거리.
first_min = BFS()

path = []
dest = N
i = temppath[N]
while i > 0:
    path.append((i, dest))
    dest = i
    i = temppath[i]

# 갔던 엣지 저장
path = path[::-1]

# 길을 하나씩 2배로 바꿨을 때 최단거리.
max_of_second_min = 0

# 전체를 다 두배로 바꿀 필요는 없음.
# 원래 최단거리에 포함되는 길만 바꾸면 됨.
for i in range(M):
    start, end, dist = roads[i]

    # 갔던 엣지만 바꾸면 됨.
    if (start, end) in path or (end, start) in path:
        roads[i][2] *= 2

        dict.clear()
        dict, dists = init(roads)

        # b = BFS()
        # print(b)
        max_of_second_min = max(max_of_second_min, BFS())
        

        roads[i][2] /= 2

print(int(max_of_second_min - first_min))