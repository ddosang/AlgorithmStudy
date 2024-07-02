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

