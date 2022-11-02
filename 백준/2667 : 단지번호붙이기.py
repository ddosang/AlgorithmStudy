import sys
from collections import deque

def BFS(i, j):
    q = deque()

    ch[i][j] = 1
    q.append((i, j))
    cnt = 1


    while q:
        i, j = q.popleft()

        for x, y in adj:
            if not 0 <= i + x < n:
                continue
            if not 0 <= j + y < n:
                continue

            if apartment[i + x][j + y] == 1 and ch[i + x][j + y] == 0:
                ch[i + x][j + y] = 1
                cnt += 1
                q.append((i + x, j + y))

    return cnt





n = int(sys.stdin.readline())
apartment = [[int(c) for c in sys.stdin.readline().strip()] for _ in range(n)]
ch = [[1 if apartment[i][j] == 0 else 0 for j in range(n)] for i in range(n)]

adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sol = []

cnt = 0
q = deque()

for i in range(n):
    for j in range(n):
        if apartment[i][j] == 1 and ch[i][j] == 0:
            sol.append(BFS(i, j))


sol.sort()
print(len(sol))
for c in sol:
    print(c)
