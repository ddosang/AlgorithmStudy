import sys
import math
readl = sys.stdin.readline

N = int(readl())
checkpoint = [list(map(int, readl().split())) for _ in range(N)]

# copy = deepcopy(checkpoint)
# 처음엔 그냥 for 문으로 하나씩 제외시키고 돌렸는데,
# 시간 초과 나서..
# dist 배열에 이전 것과의 거리차이를 다 넣어놓고,
distance = [0]
for i in range(N - 1):
    dist = abs(checkpoint[i + 1][0] - checkpoint[i][0]) + abs(checkpoint[i + 1][1] - checkpoint[i][1])
    distance.append(dist)

# 전체 더한 후,
totalDist = sum(distance)


# 어떤 하나의 점이 빠지면
# 그 이전 이후 distance 빠지는거고
# 걔가 빠진 거리를 다시 계산.
dist = 0
min_dist = math.inf
# 1번이랑 N번 빼고 건너뛰기.
for i in range(1, N - 1):
    dist = totalDist - (distance[i] + distance[i + 1]) + abs(checkpoint[i + 1][0] - checkpoint[i - 1][0]) + abs(checkpoint[i + 1][1] - checkpoint[i - 1][1])
    min_dist = min(min_dist, dist)
print(min_dist)