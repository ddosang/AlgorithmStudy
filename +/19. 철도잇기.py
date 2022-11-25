import sys
from collections import deque
readl = sys.stdin.readline

def BFS(n):
    q = deque([n])
    chk[n] = 1
    cnt = 1

    while q:
        x = q.popleft()

        # 지금 갈 수 있는 기차역을 전부 방문해본다.
        for nx in train_dict[x]:
            if chk[nx] == 1:
                continue

            chk[nx] = 1
            q.append(nx)
            cnt += 1
    
    return cnt


# 그래프의 연결성분을 구하고,
# 연결성분 제일 긴거 (k + 1) 개의 기차역 개수를 합치면 된다.

N, M, K = map(int, readl().split())
train = []
train_dict = {i:[] for i in range(1, N+1)}

# 기차가 지나다니는 길은 양방향.
# 양방향 그래프를 Dict 로 만든다.
for _ in range(M):
    s, e = map(int, readl().split())
    train_dict[s].append(e)
    train_dict[e].append(s)


chk = [0] * (N + 1)

# 원래는 각 연결성분 그래프 자체를 저장했는데, 
# 각 연결성분의 길이만 저장해도 충분.
total_graph = []

# 일단 전체 그래프를 연결성분마다 BFS 해서 길이를 저장하고,
for i in range(1, N + 1):
    if chk[i] == 0:
        total_graph.append(BFS(i))

total_graph.sort(key=lambda x:-x)


sol = 0
# 더 놓을 수 있는 다리가 K 개면 연결성분 K + 1개 까지 이을 수 있음.
# 근데 연결성분이 그거보다 적으면 그냥 전체를 더한걸로 끝내야됨.
if K + 1 >= len(total_graph):
    sol = sum(total_graph)
else:
    sol = sum(total_graph[:K+1])

print(sol)