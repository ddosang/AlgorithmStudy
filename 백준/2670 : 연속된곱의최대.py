import sys
from functools import reduce

readl = sys.stdin.readline

n = int(readl())
arr = [float(readl()) for _ in range(n)]

# 연속된 곱의 최대.
sol = 0

# 곱 = 1
# for i in range(2, n + 1):
#     for j in range(0, n - i):
#         곱 = reduce(lambda acc, cur: acc * cur, arr[j:j + i])
#         # print(곱)
#         if 곱 > sol:
#             sol = 곱

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i] = max(dp[i - 1] * arr[i], arr[i])

    if sol < dp[i]:
        sol = dp[i]



print(f"{sol:.3f}")
