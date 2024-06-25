# 혼자 푼거 1 : 마지막 케이스 시간 초과
c, n = map(int, input().split())
dogs = [int(input()) for _ in range(n)]

def DFS(level, weight):
    if level == n:
        if weight <= c:
            weights.append(weight)

    else:
        DFS(level + 1, weight + dogs[level])
        DFS(level + 1, weight)

weights = []
DFS(0, 0)
print(max(weights))



# 혼자 푼거 2: 마지막 케이스 때문에 더하는거 말고 전체 합에서 빼는 것으로 바꿈.
# 근데 만약 n 이 엄청 작게 주어지면?? 결국 시간 초과가 날 것이다...
# 전역 변수 듣고 바꿈. -> list 는 왜 global 안써도 되는거지? 해당 리스트 자체를 생성하는게 아니니까.
c, n = map(int, input().split())
dogs = [int(input()) for _ in range(n)]

def DFS(level, weight):
    global max_weight
    if weight <= c:
        if max_weight < weight:
            max_weight = weight
        return

    if level == n:
        if weight <= c and max_weight < weight:
            max_weight = weight

    else:
        DFS(level + 1, weight)
        DFS(level + 1, weight - dogs[level])

max_weight = 0
DFS(0, sum(dogs))
print(max_weight)



# 강의 듣고 - 쳐낼 수 있는 분기를 한번 더 쳐낸다.
c, n = map(int, input().split())
dogs = [int(input()) for _ in range(n)]

def DFS(level, weight, tsum):
    global max_weight
    if weight + (total - tsum) < max_weight:
        return

    if weight > c:
        return

    if level == n:
        if weight > max_weight:
            max_weight = weight

    else:
        tsum += dogs[level]
        DFS(level + 1, weight + dogs[level], tsum)
        DFS(level + 1, weight, tsum)


total = sum(dogs)
max_weight = 0
DFS(0, 0, 0)
print(max_weight)



# 240625 복습
import sys
input = sys.stdin.readline


def DFS(level, tot):
    global max_baduk

    # 무게를 초과해버리면 검사할 필요 없음. 
    if tot > C:
        return

    # 최대 무게가 나오면 그 이상 검사할 필요 없음.
    if tot == C:
        print(sum)
        exit(0)
        return
    
    # 앞으로 들어갈 걸 다 합쳐도 지금 max 보다 작으면 검사할 필요 X.
    if max_baduk > tot + sum(dogs[level:]):
        return

    # DFS 로 더할 수 있을 만큼 더했으면 거기서 max 저장.
    if level == N:
        max_baduk = max(max_baduk, tot)
        return
    

    DFS(level + 1, tot + dogs[level])
    DFS(level + 1, tot)



C, N = map(int, input().split())
dogs = [int(input()) for _ in range(N)]
dogs.sort(key=lambda x:-x)
total = sum(dogs)
max_baduk = 0

# 다 태운게 더 작으면 굳이 검사할 필요도 없음.
if total <= C:
    print(total)
    exit(0)

DFS(0, 0)
print(max_baduk)
