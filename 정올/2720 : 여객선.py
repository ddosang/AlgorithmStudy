import sys
sys.setrecursionlimit(10**6)
readl = sys.stdin.readline

# 배에 몇번째부터 몇번째까지 가능한지 탐색.
def findPeople(s, pivot):
    start = s
    end = N
    sol = -1
    while start <= end:
        mid = (start + end) // 2

        w = psum[mid] - psum[s]
        if w > pivot:
            end = mid - 1
        elif w == pivot:
            return mid
        else:
            start = mid + 1
            sol = mid
    return sol

def DFS(level, totalShip, s):
    global max_remain

    if totalShip <= max_remain:
        return
    
    if level >= N:
        # print(max_remain)
        max_remain = totalShip
        return
    
    # 배를 기준으로 1번 배, 2번 배, 3번 배 각각에서 가지를 뻗어봄.
    # ch 이용해서 한번 탄 배에 다시 타진 않도록.
    for i in range(B):
        if ch[i]: 
            continue
        end = findPeople(s, ships[i])
        if end == -1: 
            continue
        
        ch[i] = 1
        DFS(level + (end - s), totalShip - ships[i], end)
        ch[i] = 0



B, N = map(int, readl().split())
ships = [int(readl()) for _ in range(B)]
weights = [int(readl()) for _ in range(N)]
psum = [0] * (N + 1)
ch = [0] * B

for i, w in enumerate(weights):
    psum[i + 1] = psum[i] + w

if psum[N] > sum(ships):
    print(-1)
    exit(0)

max_remain = -1
DFS(0, sum(ships), 0)
print(max_remain)