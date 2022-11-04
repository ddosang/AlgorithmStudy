def BFS(i, j):
    q = deque()
    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ch = [[0] * w for _ in range(h)] # 이걸 여기로 안넣어서 계속 뭔가 다른 값이 나왔는데,

    q.append((i, j, 0))
    ch[i][j] = 1

    while q:
        x, y, dist = q.popleft()
        # print(x, y, ch[x][y])
        for dx, dy in adj:
            nx = dx + x
            ny = dy + y

            if not 0 <= nx < h:
                continue
            if not 0 <= ny < w:
                continue

            # 육지가 아니라면
            if pmap[nx][ny] == "W":
                continue

            if ch[nx][ny] != 0:
                continue

            ch[nx][ny] = 1
            # 방금 탐색한 것과 이전까지의 최댓값 중 더 큰걸 담아야됨.
            q.append((nx, ny, dist + 1))

    return dist # 처음에 1로 시작하니까.

readl = sys.stdin.readline
h, w = map(int, readl().split())
pmap = [[c for c in readl().strip()] for _ in range(h)]

max_dist = 0
# BFS 로 탐색해서 성분 찾고, 그 중 최단거리가 최대인 것을 찾으면 될듯...?
for i in range(h):
    for j in range(w):
        # 다른 BFS 처럼 하나의 지점에서 시작해서 그것과 이어진 지점을 한번 돌고 끝나는게 아니라,
        # 모든 육지에 대해서 BFS 를 수행하고 (그래프 하나에도 여러번 접근)
        # 가장 먼 곳을 찾아서 그 곳의 거리 중 가장 큰 것을 찾는다.
        if pmap[i][j] == "L": # 여기서 ch 는 검사를 안하니까!!
            max_dist = max(max_dist, BFS(i, j))

print(max_dist)
