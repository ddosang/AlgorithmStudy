import sys

def DFS(level, cost):
    global min_cost

    if level == N:
        # 마지막에 집으로 돌아와야함.
        # 집으로 돌아오는 길 비용이 0이면 길이 없음.. cost 를 크게 만들어서 답이 될 수 없게 함.
        if costs[res[level - 1]][0] == 0:
            cost = 1200
        cost += costs[res[level - 1]][0]

        if min_cost > cost:
            min_cost = cost
        return

    if min_cost <= cost:
        return

    # 0을 제외하고 순서를 만들어주면 된다.
    for i in range(1, N):
        if ch[i] == 0:
            # 만약 중간 길이 0이면 갈 수 없으므로 거기서 더 가지를 칠 필요가 없음.
            if costs[res[level - 1]][i] == 0:
                continue
            res[level] = i
            ch[i] = 1
            DFS(level + 1, cost + costs[res[level - 1]][i])
            ch[i] = 0



N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_cost = 1200

ch = [0] * N
ch[0] = 1 # 0 (집) 에서 출발.
res = [0] * N

DFS(1, 0) # 젤 처음이 정해져있으니까 넣고 시작.
print(min_cost)
