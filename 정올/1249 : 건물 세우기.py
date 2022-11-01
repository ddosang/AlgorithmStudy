import sys

def DFS(level, cost):
    global min_cost

    # 없이 했더니 시간 초과 나서 추가. 지금까지의 최솟값보다 더 크면 더 볼 필요 없음.
    if cost >= min_cost:
        return

    if level == n:
        if min_cost > cost:
            min_cost = cost
            total.append([cost, res.copy()])
        return

    for i in range(n):
        # ch 이용해서 같은 것을 또 넣지 않도록!
        if ch[i] == 0:
            ch[i] = 1
            res[level] = i
            DFS(level + 1, cost + building[level][i])
            ch[i] = 0


n = int(sys.stdin.readline())
building = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_cost = 1000 # 100 미만 건물 10개 니까 1000 보다 클 수 없음.
res = [0] * n
ch = [0] * n
total = []


DFS(0, 0)
print(min_cost)

for t in total:
    if t[0] == min_cost:
        for i in range(n):
            print(t[1][i] + 1, end=' ')
