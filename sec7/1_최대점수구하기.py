# 240701 풀이
def DFS(level, total_score, total_time, start):
    global max_score
    if total_time > M:
        return
    
    max_score = max(max_score, total_score)

    if total_time == M:
        return

    if level == N:
        return
    
    # start 추가 안했을 때는 3번 예제에서 timeout
    for i in range(start, N):
        score, time = scores[i]
        if not visited[i]:
            visited[i] = True
            DFS(level + 1, total_score + score, total_time + time, i + 1)
            visited[i] = False


N, M = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
visited = [0] * N

DFS(0, 0, 0, 0)
print(max_score)
