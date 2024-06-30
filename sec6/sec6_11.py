n, k = map(int, input().split())
arr = list(map(int, input().split()))
num = int(input())

def DFS(level, start, sum):
    global cnt

    if level == k:
        if sum % num == 0:
            cnt += 1

    else:
        for i in range(start, n):
            res[level] = arr[i]
            DFS(level + 1, i + 1, sum + arr[i])



res = [0] * k
cnt = 0

DFS(0, 0, 0)

print(cnt)


## itertools combination 사용

from itertools import combinations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())

cnt = 0

for c in combinations(arr, k):
    if sum(c) % m == 0:
        cnt += 1

print(cnt)


# 240701 복습
from itertools import combinations

import sys
input = sys.stdin.readline


def DFS(level, sum, start):
    global cnt

    if level == K:
        if sum % M == 0:
            cnt += 1
        return
    

    for i in range(start, N):
        DFS(level + 1, sum + nums[i], i + 1)


N, K = map(int, input().split())
nums = list(map(int, input().split()))
M = int(input())
cnt = 0

DFS(0, 0, 0)

# for li in combinations(nums, K):
#     print(li)
#     if sum(li) % M == 0:
#         cnt += 1

print(cnt)
