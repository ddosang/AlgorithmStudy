import sys

def DFS(n, m, level):
    if level == n:
        for i in range(n):
            print(order[i], end=' ')
        print()
        return

    if m == 1:
        for j in range(1, 7):
            order[level] = j
            DFS(n, m, level + 1)
    elif m == 2:
        for j in range(1, 7):
            if level == 0:
                order[level] = j
                DFS(n, m, level + 1)
            # 겹치는게 나오면 안되니까 이전 것보다 크거나 같을 때만 넣어야 함. 1 1 2 -> 2 1 1 이렇게 되지 않고 2 2 2 부터 시작하게
            elif level > 0 and order[level - 1] <= j:
                order[level] = j
                DFS(n, m, level + 1)
    elif m == 3:
        for j in range(1, 7):
            # 다 달라야 하니까 앞에 없는 것만 가능
            if not (j in order[:level]):
                order[level] = j
                DFS(n, m, level + 1)





n, m = map(int, sys.stdin.readline().split())
order = [0] * n

DFS(n, m, 0)
