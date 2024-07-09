# 240701 풀이

def DFS(level, total, start):
    global max_price
    if start > N:
        return
    
    # print(res, total)
    max_price = max(max_price, total)

    if level == N:
        return
    
    for i in range(start, N):
        res[level] = i
        DFS(level + 1, total + council[i][1], i + council[i][0])



N = int(input())
council = [list(map(int, input().split())) for _ in range(N)]
max_price = 0
res = [0] * N

DFS(0, 0, 0)
print(max_price)


# 240709 강의 코드

N = int(input())
councils = [list(map(int, input().split())) for _ in range(N)]
max_cost = 0

def DFS(level, cost):
    global max_cost
    if level == N:
        max_cost = max(cost, max_cost)
        return
    
    # 날짜를 level 로 사용. 이번걸 선택하고
    if level + councils[level][0] < N:
        DFS(level + councils[level][0], cost + councils[level][1])
    # 이번걸 선택하지 않고.
    DFS(level + 1, cost)


DFS(0, 0)
print(max_cost)
