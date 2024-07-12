# 카데고리가 BFS 라서 BFS 로 시도했는데 뒷쪽 케이스에서 시간이 너무 오래 걸려서 보니까
# 굳이 BFS 를 이용할 필요가 없었던게 일차선에서 -1, 1, 5 만큼 이동할 수 있으니
# 최소만큼 이동하려면 당연히.. 5 로 최대한 이동한 다음에,
# 1 2 3 4 만큼 남았을 때 1 2 3 은 1로 1번 2번 3번 / 4는 5, -1 로 2번 이동이 이득이니
# 단순 계산으로 처리하면 됨.

S, E = map(int, input().split())
if S < E:
    cnt = (E - S) // 5
    cnt += 2 if ((E - S) % 5 == 4) else (E - S) % 5
else:
    cnt = S - E

print(cnt)



# 강의 코드
from collections import deque

def BFS(S):
    global cnt
    q = deque()

    q.append((S, 0))
    visited[0] = 1

    while q:
        x, current = q.popleft()

        if x == E:
            print(current)
            return

        for dx in [-1, 1, 5]:
            if x + dx <= 0 or x + dx > 10000:
                continue

            if ((x + dx) in visited.keys()):
                continue

            q.append((x + dx, current + 1))
            visited[x + dx] = 1  # visited 체크를 여기서 해야 시간복잡도에 안걸림.
        # print(q)


S, E = map(int, input().split())

visited = {} # 강의에선 그냥 ch = [0] * 10001 로 함.
BFS(S)
