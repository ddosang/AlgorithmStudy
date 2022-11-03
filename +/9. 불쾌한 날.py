import sys
from collections import deque

readl = sys.stdin.readline

n = int(readl())
cows = [int(readl()) for _ in range(n)]

stack = []
cnt = 0

for cow in cows:
    if len(stack) == 0:
        stack.append(cow)

    while stack and stack[-1] <= cow:
        stack.pop()

    cnt += len(stack)
    stack.append(cow)


print(cnt)
