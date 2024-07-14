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


# 240714 강의 방법
# 굳이 visited 배열을 따로 둘 필요가 없는 문제였다.
# 대신 dis 배열은 따로 두고 품. 
from collections import deque

arr = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < 7 and 0 <= y + dy < 7 and arr[x + dx][y + dy] == 0:
            q.append((x + dx, y + dy))
            arr[x + dx][y + dy] = 1
            dis[x + dx][y + dy] = dis[x][y] + 1


print(-1 if dis[6][6] == 0 else dis[6][6])

