import sys
sys.setrecursionlimit(10 ** 6)
readl = sys.stdin.readline

# 사건 번호를 기준으로 어디 있는지를 판단.
def DP(level, firstIdx, secondIdx):
    
    if level >= W:
        return 0
    
    if dp[firstIdx][secondIdx]:
        return dp[firstIdx][secondIdx]

    
    first = accidents[firstIdx] if firstIdx > -1 else (1, 1)
    second = accidents[secondIdx] if secondIdx > -1 else (N, N)
    r, c = accidents[level]

    dp[firstIdx][secondIdx] = min(abs(r - first[0]) + abs(c - first[1]) + DP(level + 1, level, secondIdx)
        , abs(r - second[0]) + abs(c - second[1]) + DP(level + 1, firstIdx, level)) 
    
    return dp[firstIdx][secondIdx]


# DP 함수도 level 없이 firstIdx, secondIdx 의 max 만 가지고 확인 가능.
def path(firstIdx, secondIdx):
    if firstIdx == W - 1 or secondIdx == W - 1:
        return
    
    # 다음 사건 번호.
    nextIdx = max(firstIdx, secondIdx) + 1

    first = accidents[firstIdx] if firstIdx > -1 else (1, 1)
    second = accidents[secondIdx] if secondIdx > -1 else (N, N)

    # print(nextIdx)
    r, c = accidents[nextIdx]
    firstDist = abs(r - first[0]) + abs(c - first[1]) + DP(nextIdx, nextIdx, secondIdx)
    secondDist = abs(r - second[0]) + abs(c - second[1]) + DP(nextIdx, firstIdx, nextIdx)

    if firstDist > secondDist:
        print(2)
        path(firstIdx, nextIdx)
    else:
        print(1)
        path(nextIdx, secondIdx)




# def DFS(level, first, second, sum):
#     global min_dist

#     if sum >= min_dist:
#         return

#     if level == W:
#         if min_dist > sum:
#             min_dist = sum
#         return
    

#     r, c = accidents[level]

#     # 첫번째보다 왼쪽 위에 있는것만 아니면 두번째를 움직여봐야됨.
#     if not (first[0] >= r and first[1] >= c):
#         DFS(level + 1, first, accidents[level], sum + abs(r - second[0]) + abs(c - second[1]))
        
#     # 두번째보다 오른쪽 아래에 있는 것만 아니면 첫번째를 움직여봐야됨.
#     if not (second[0] <= r and second[0] <= c):
#         DFS(level + 1, accidents[level], second, sum + abs(r - first[0]) + abs(c - first[1]))


N = int(readl())
W = int(readl())
accidents = [list(map(int, readl().split())) for _ in range(W)]

res = [0] * W

# (1, 1), (N, N)
first = (1, 1)
second = (N, N)
dp = [[0] * (W + 1) for _ in range(W + 1)]

print(DP(0, -1, -1))
path(-1, -1)
# print(*res, end='\n')

# min_dist = 2001 * 20
# DFS(0, first, second, 0)
# print(min_dist)