import sys
readl = sys.stdin.readline

def DFS(level, sum, start):
    global min_height
    if sum >= B:
        if min_height > sum:
            min_height = sum
        return

    if level == N:
        if sum >= B and min_height > sum:
            min_height = sum
        return
    
    if sum < B:
        for i in range(start, N):
            h = heights[i]
            res[i] = h
            DFS(level + 1, sum + h, i + 1)



T = int(readl())
for _ in range(T):
    N, B = map(int, readl().split()) # 소의 마리수 N, 책꽂이 높이 B
    heights = [int(readl()) for _ in range(N)]

    ch = [0] * N
    res = [0] * N
    min_height = 1000001
    DFS(0, 0, 0)
    print(min_height - B)

