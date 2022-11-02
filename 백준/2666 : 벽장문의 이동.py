import sys

def solved(door1, door2, index):
    if index == t:
        return 0

    target = useOrder[index]
    dp[door1][door2][index] = min(abs(door1 - target) + solved(target, door2, index + 1),
                                  abs(door2 - target) + solved(door1, target, index + 1))

    return dp[door1][door2][index]



n = int(sys.stdin.readline())
open1, open2 = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
useOrder = [int(sys.stdin.readline()) for _ in range(t)]

dp = [[[0] * 21] * 21] * 21
dp = [[[0] * (order_n) for _ in range(n + 1)] for _ in range(n + 1)]

print(solved(open1, open2, 0))
