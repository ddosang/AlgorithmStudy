import sys
readl = sys.stdin.readline

def upper(n, m):
    sn = list(str(n))[::-1]
    sm = list(str(m))[::-1]

    # max_len = max(len(sn), len(sm))
    min_len = min(len(sn), len(sm))

    # 자리 올림이 발생하면 False
    for i in range(min_len):
        if int(sn[i]) + int(sm[i]) >= 10:
            return False

    # 자리 올림이 발생하지 않으면 True
    return True



def DFS(level, weight, cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    
    # 지금까지 찾은 그룹 + 앞으로 할 레벨의 수 가
    # 지금까지 찾은 가능한 가장 큰 소 그룹보다 개수가 작다면 굳이 할 필요 없음.
    if cnt + (N - level) <= max_cnt:
        return

    if level == N:
        # print(*res, cnt)
        return

    
    # 자리올림이 안 생기면 넣는것도 가고 안넣는 것도 가고,
    if upper(weight, cows[level]):
        res[level] = level
        DFS(level + 1, weight + cows[level], cnt + 1)

    # 자리올림이 생기면 안넣는거만 감.
    DFS(level + 1, weight, cnt)


N = int(readl())
cows = [int(readl()) for _ in range(N)]

ch = [0] * N
res = [-1] * N
max_cnt = 0
DFS(0, 0, 0)
print(max_cnt)