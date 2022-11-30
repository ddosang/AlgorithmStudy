import sys
from copy import deepcopy
readl = sys.stdin.readline

def check(level, W):
    total = 0

    # 앞으로 검사할 동전을 다 합쳤을 때,
    # W 보다 작으면 검사할 필요가 없음.
    for i in range(level, 6):
        total += coins[i] * 금액[i]
    
    return total >= W
    

# 6개의 동전을 500원부터 하나씩 내려가는 것이 level
def DFS(level, W, cnt):
    global max_cnt, max_coins

    if not check(level, W):
        return

    if W < 0:
        return
    
    if W == 0:
        if max_cnt < cnt:
            max_cnt = cnt
            max_coins = deepcopy(coins)
        return

    if level == 6:
        if W == 0 and max_cnt < cnt:
            max_cnt = cnt
            max_coins = deepcopy(coins)
        return
    
        
    # 해당 동전을 몇개 사용할건지.
    for i in range(coins[level] + 1):
        if W < 금액[level] * i:
            break
        W -= i * 금액[level]
        coins[level] -= i
        DFS(level + 1, W, cnt + i)
        W += i * 금액[level]
        coins[level] += i
    


W = int(readl())
coins = list(map(int, readl().split()))
금액 = [500, 100, 50, 10, 5, 1]

max_coins = [0] * 6
max_cnt = 0
DFS(0, W, 0)
for i in range(6):
    max_coins[i] = coins[i] - max_coins[i]
print(max_cnt)
print(*max_coins)