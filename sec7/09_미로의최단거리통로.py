from collections import deque

arr = [list(map(int, input().split())) for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]

q = deque()
q.append((0, 0, 0))

while q:
    x, y, dist = q.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < 7 and 0 <= y + dy < 7 and (not visited[x + dx][y + dy]) and arr[x + dx][y + dy] == 0:
            q.append((x + dx, y + dy, dist + 1))
            visited[x + dx][y + dy] = True
            if x + dx == 6 and y + dy == 6:
                print(dist + 1)
                exit(0)
                
print(-1)

