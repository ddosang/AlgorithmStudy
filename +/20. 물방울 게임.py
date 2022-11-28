import sys
readl = sys.stdin.readline

def DFS(level, sum, cnt):
    global min_cnt

    if level == N:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    
    if cnt >= min_cnt:
        return
    
    # 하나의 스킬은 양의 정수 크기의 물방울 한개를 생성 할 수 있고
    # 또 다른 스킬은 현재 존재하는 물방울 하나를 제거하는 스킬
    
    # 유저 물방울이 더 크면 스킬 안쓰고 가고
    if sum > waterDrops[level]:
        DFS(level + 1, sum + waterDrops[level], cnt)

    # 유저 물방울이 더 작으면 스킬 쓰고 가고
    else:
        # 1. 생성 : 먹을 수 있는 크기의 물방울을 생성해야함. -> 먹을 수 있는 최대 크기로 생성.
        # 포인트 : 생성 시 level 은 그대로!!!!
        if sum > 1:
            DFS(level, sum + (sum - 1), cnt + 1)
        DFS(level + 1, sum, cnt + 1)



T = int(readl())
for i in range(T):
    A, N = map(int, readl().split())
    waterDrops = list(map(int, readl().split()))
    waterDrops.sort()

    min_cnt = 101
    # 유저 물방울이 필드 물방울보다 크면 흡수 가능.
    DFS(0, A, 0)

    print("Case #" + str(i + 1) + ": " + str(min_cnt))