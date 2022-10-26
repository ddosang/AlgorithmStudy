import sys
from collections import deque

def BFS():
    start = 0
    end = M - 1

    q = deque()
    q.append((start, 0)) # 1번역에서 시작 time 0
    min_map[start] = 0


    while q:
        local_start, time = q.popleft()

        # 중간에 바뀐게 더 작으면 할 필요 없음.
        if min_map[local_start] < time:
            continue

        for local_end in range(N):
            ntime = time + subway_map[local_start][local_end]


            if min_map[local_end] <= ntime:
                continue

            # 새로운 루트 (다른 곳을 거쳐 감) 이 더 작으면 바꿈.
            q.append((local_end, ntime))
            min_map[local_end] = ntime
            route[local_end] = local_start # 거쳐가는 목적지에 출발지를 저장.
            # route[local_start] = local_end # 이렇게 하면 중간에 목적지까지 가지 않지만 최솟값이 갱신되는 경로에서 값이 바뀌어서 답이 안나옴.


N, M = map(int, sys.stdin.readline().split())
subway_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start = 0


min_map = [99999999] * N
route = [-1] * N

BFS()

print(min_map[M - 1])
# print(route)

j = M - 1
arr = []
# 반대로 뽑으면 됨
while j >= 0:
    arr.append(j)
    j = route[j]

for i in range(len(arr)):
    print(arr[len(arr) - 1 - i] + 1, end=' ')
