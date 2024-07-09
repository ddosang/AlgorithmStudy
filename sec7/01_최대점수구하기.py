# 240701 풀이
# 첫번째 가지 : 1번 풀고           / 2번 풀고      / 3번 풀고 / 4번 풀고 / 5번 풀고
# 두번쨰 가지 : 2     3    4   5 /  3     4  5 /  4 5   /  5
# 세번쨰 가지 : 345 / 45 / 5     // 4 5 / 5   //  5 
# 1번을 아예 안 푸는게 경우의 수에 없네..?

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


# 240709 강의 코드
# n 번 문제를 풀고 안풀고
N, M = map(int, input().split())
quizes = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

def DFS(level, score, time):
    global max_score
    if time > M:
        return
    
    if level == N:
        max_score = max(score, max_score)
        return
    
    DFS(level + 1, score + quizes[level][0], time + quizes[level][1])
    DFS(level + 1, score, time)


DFS(0, 0, 0)
print(max_score)
    
