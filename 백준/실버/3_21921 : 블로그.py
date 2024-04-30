import sys
input = sys.stdin.readline

N, X = map(int, input().split())
views = list(map(int, input().split()))

lt = 0
rt = X
local = sum(views[lt:rt]) # 구간
max_local = local # 가장 큰 방문자 수
max_local_cnt = 1 # 가장 큰 방문자 수인 기간이 몇 번 있는지

while rt < N:
    local -= views[lt] 
    local += views[rt]

    lt += 1
    rt += 1

    if max_local == local:
        max_local_cnt += 1 # 가장 큰거랑 같으면 cnt 늘리다가
    elif max_local < local:
        max_local = local
        max_local_cnt = 1 # 더 큰게 나오면 갱신

if max_local > 0:
    print(max_local)
    print(max_local_cnt)
else:
    print("SAD")
