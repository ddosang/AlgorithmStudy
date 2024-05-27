import sys
import copy
from itertools import combinations as cb
input = sys.stdin.readline

# 두 점 사이의 거리를 구하는 함수
def dist(home_x, home_y, chicken_x, chicken_y):
    return abs(home_x - chicken_x) + abs(home_y - chicken_y)

# 집 목록과 치킨 목록을 가지고,
# 현재 최소 치킨 거리를 구할 때 선택된 치킨집 개수와 치킨 거리를 구하는 함수
def dist_chicken(homes, chickens):
    dic = {}
    for hx, hy in homes: 
        for cx, cy in chickens:
            d = dist(hx, hy, cx, cy)

            # 집에서 가장 가까운 치킨집 저장.
            if not ((hx, hy) in dic.keys()):
                dic[(hx, hy)] = (cx, cy, d)
            elif d < dic[(hx, hy)][2]:
                dic[(hx, hy)] = (cx, cy, d)

    chicken_candidates = set()
    chicken_dist = 0
    # 저장된 집에서 꺼내와서 거리 계산
    for key, val in dic.items():
        chicken_candidates.add((val[0], val[1]))
        chicken_dist += val[2]

    return len(chicken_candidates), chicken_dist


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 입력 처리
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))


# 최소 치킨 거리 한번 구해봄.
candidates_cnt, chicken_dist = dist_chicken(homes, chickens)

# 여기서 선택된 치킨집이 M 개보다 작으면 그렇게 끝내면 됨.
if candidates_cnt <= M:
    print(chicken_dist)
    exit(0)

# 그렇지 않으면 M 개를 선택해서 각 집과의 치킨거리를 구해보고 그 중 최솟값
chicken_dist = 101 * 2500
for chks in cb(chickens, M):
    _, temp = dist_chicken(homes, chks)
    chicken_dist = min(temp, chicken_dist)

print(chicken_dist)
