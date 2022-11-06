import sys
from collections import deque

sys.setrecursionlimit(10**6)

readl = sys.stdin.readline

def DP(l, r):
    if l == n or r == n:
        return 0

    # 이미 계산된 값이면 그 값을 return
    if dp[l][r] != -1:
        return dp[l][r]

    dp[l][r] = 0
    if right[r] < left[l]:
        dp[l][r] += right[r] + DP(l, r + 1)
    else:
        dp[l][r] += max(DP(l + 1, r), DP(l + 1, r + 1))

    return dp[l][r]


n = int(readl())
left = list(map(int, readl().split()))
right = list(map(int, readl().split()))

dp = [[-1] * n for _ in range(n)]


print(DP(0, 0))
