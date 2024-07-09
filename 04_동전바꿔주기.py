# 풀이 : 3번 케이스 약간 느림.
T = int(input())
K = int(input())
coins = [list(map(int, input().split())) for _ in range(K)] # 금액 / 개수
cnt = 0

def DFS(level, cost):
    global cnt
    
    if cost == T:
        cnt += 1
        return

    if level == K:
        return
    
    for i in range(coins[level][1] + 1):
        new_cost = cost + coins[level][0] * i
        if new_cost > T:
            break

        DFS(level + 1, new_cost)
        


DFS(0, 0)
print(cnt)
