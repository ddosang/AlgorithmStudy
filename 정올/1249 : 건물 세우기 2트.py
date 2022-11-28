import sys
from copy import deepcopy
readl = sys.stdin.readline

def DFS(level, sum):
    global min_cost, min_res

    if sum >= min_cost:
        return

    if level == n:
        if sum <= min_cost:
            min_cost = sum
            min_res = deepcopy(res)
        return
    
    for i in range(n):
        cost = buildings[level][i]
        
        if ch[i] == 0:
            ch[i] = 1
            res[level] = i + 1
            DFS(level + 1, sum + cost)
            ch[i] = 0


n = int(readl())
buildings = [list(map(int, readl().split())) for _ in range(n)]

min_cost = 100 * n
min_res = [0] * n
res = [0] * n
ch = [0] * n
DFS(0, 0)
print(min_cost)
print(*min_res)