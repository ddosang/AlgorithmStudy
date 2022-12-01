import sys
from collections import deque
readl = sys.stdin.readline


def DFS(level, next_num):
    # 그래서 그래프의 끝에 다다르면
    # 파고든 경로를 res 에 저장 -> new 에 저장.
    # 예를 들어서 테케에서 1 2 3 5 / 1 2 4 / 1 4 / 1 5 를 가지고 있음.
    if next_num != 1 and len(graph[next_num]) == 0:
        cnt = 1
        idx = 1

        # 이 문제의 관건은 트리의 같은 레벨일 때, 그냥 레벨 순서대로 주는걸로 생각 할 수 있는데,
        # 가지1 : 상하관계가 어떤 노드에는 있고 어떤 노드에는 없으므로, 자식이 많은 녀석에게 큰걸 먼저 배분해야 된다는 것임.

        # 원래는 그렇게 해서 1 2 3 5 같은 경우 자식이 본인 포함 4개 3개 2개 1개 이렇게 저장해서 주려고 했더니... 

        # for i, x in enumerate(res[:level]):
        #     chk[x] = max(chk[x], level - i)

        # 이렇게 했을 때의 문제점.. 지금 보는 트리에 포함되지 않은 부모는 숫자가 같이 안바뀐다는거임...
        # 1 9 3 5 6 10
        # 1 7 5 6 10
        # 이러면 1 7 5 도 자식이 더 많은 걸로 취급이 되어야 하는데 그렇지가 않음. -> 그래서 res 에서 바로 처리 안하고 new 로 빼서 처리.

        # 가지2 : 거기에다가 자식 개수가 똑같을 때, 상사가 받은 보너스보다 자기가 작을 수 있게 배분해야 함.

        new.append(res[:level])

            
        return

    # DFS 를 이용해서 깊이 우선 탐색을 진행한다.
    for next in graph[next_num]:
        res[level] = next
        DFS(level + 1, next)
        res[level] = 0



N, M = map(int, readl().split())
graph = {(i + 1):[] for i in range(N)}
upgraph = {(i + 1):[] for i in range(N)}

for _ in range(M):
    s, e = map(int, readl().split())
    graph[s].append(e)
    upgraph[e].append(s)
bonus = sorted(list(map(int, readl().split())), reverse=True)

# print(graph)
new = []


res = [0] * (N + 1)
chk = [0] * (N + 1)
res[0] = 1
sol = [0] * (N + 1)
DFS(1, 1)
# chk.pop(0)
# chk = sorted(list(enumerate(chk, 1)), key=lambda x:-x[1])


# 헷갈림 1 : 자식 개수 세기.
chk = [0] * (N + 1)
# print(*new)
for i in range(len(new)):
    cnt = 0
    for n in new[i][::-1]:
        cnt += 1

        if chk[n] != 0:
            # 이미 헤아린 어떤 트리의 자식이었다면.
            cnt = max(chk[n], cnt) 
        
        chk[n] = max(chk[n], cnt)

    # print(chk)


chk.pop(0)
chk = sorted(list(enumerate(chk, 1)), key=lambda x:-x[1])


for i in range(N):
    # 헷갈림 2 : 부모가 받는 것보다 크면
    breaked = False
    for j in upgraph[chk[i][0]]:
        if sol[j] <= bonus[i]:
            breaked = True
            break

    # 안 작은거랑 바꿔치기 해서 준다.
    if breaked:
        k = i
        while sol[j] <= bonus[k]:
            k += 1
        bonus[i], bonus[k] = bonus[k], bonus[i]

    sol[chk[i][0]] = bonus[i]

print(*sol[1:])