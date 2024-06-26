# 혼자 푼 거
# 3, 4, 5 번 시간 초과
# 가지를 더 치면 좋을 것 같은데 어디서 쳐야할지 모르겠다.... 고 생각하던 와중 성공!
# 다른 문제처럼 레벨이 균등하게 들어가진 않고,
# 계속 들어가보다가 금액보다 커지면 위로 돌아오는 식으로 구현했다.
# 여기서 level 은 동전의 현재 개수!
def DFS(level, total):
    global min_count

    if level >= min_count:
        return

    if total > money:
        return

    elif total == money:
        if min_count > level:
            min_count = level
        return

    else:
        for coin in coins:
            DFS(level + 1, total + coin)


n = int(input())
coins = list(map(int, input().split()))
money = int(input())
min_count = money # 만약에 동전의 종류까지 다 출력하라고 한다면? min_count 가 아니라 res 배열 선언해서 res[level] = coin

coins.sort(reverse=True) # 큰거부터 가는게 효율적일거라고 생각해서 뒤집어 정렬.
count = 0

DFS(0, 0)

print(min_count)



# 240626 복습
# 예시에서 1 2 5 로 15 를 만들어야 해서
# 5 -> 3 2 1 0 개 쓸 수 있음
# 2 -> 7 6 5 4 3 2 1 0 개 쓸 수 있음
# 1 -> 15 ~ 0 개 쓸 수 있음
# 이렇게 종류를 가지고 들어가서 DFS 로 탐색.
import sys
input = sys.stdin.readline

N = int(input())
coins = list(map(int, input().split()))
coins.sort(key=lambda x:-x)
fee = int(input())
ch = [0] * N
min_cnt = fee // coins[-1] + 1

def DFS(level, current):
    global min_cnt
    if sum(ch) > min_cnt: # 이 가지를 처음에 안쳐서 4, 5 번 시간 초과
        return

    if current > fee:
        return
    
    if current == fee:
        # print(ch)
        min_cnt = min(min_cnt, sum(ch))
        return

    if level == N:
        # print(ch)
        return
    

    for i in range(int((fee - current) / coins[level]) + 1, -1, -1):
        ch[level] = i
        DFS(level + 1, current + coins[level] * i)



DFS(0, 0)
print(min_cnt)
