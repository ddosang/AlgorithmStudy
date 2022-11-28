import sys
from copy import deepcopy
readl = sys.stdin.readline

# 2의 제곱수(1~2^n) 의 합이 N 이 되는 수식을 만든다.
# 수식의 가치는 (사용된 2의 제곱수 항의 가치 합계) + (사용한 항의 개수 * 항 하나 당 추가 가치)

# level : 0 ~ 6 
# 2^(6 - level) 로 2^6 ~ 2^0 까지 각각 몇개씩 들어갈지 계산. 
def DFS(level, now):
    global max_cost, max_res
    # 만약에 2^5 ~ 2^6 - 1 이면 2^5 ~ 2^0 까지 6개 사용 가능.
    if now == 0:
        cost = 0
        for i in range(7):
            # 가치.
            if res[i] > 4:
                cost += over5[i] * res[i]
            else:
                cost += under4[i] * res[i]

        # 추가 가치.
        cost += sum(res) * A

        if max_cost < cost:
            max_cost = cost
            max_res = deepcopy(res)
        return
    
    if now < 0:
        return

    if level >= 7:
        return
    
    # 이번 level 꺼 안빼고 다음꺼 빼러 넘어감.
    DFS(level + 1, now)

    # 이번 level 꺼 빼고 기록한 뒤 다음 level 로 넘어감
    if now >= 2 ** (6 - level):
        now -= 2 ** (6 - level)
        res[6 - level] += 1
        DFS(level, now)
        res[6 - level] = 0

    # DFS(level + 1, now)




N = int(readl())
under4 = list(map(int, readl().split()))
over5 = list(map(int, readl().split()))
A = int(readl())


# limit = 0
# n = N
# while n > 0:
#     n //= 2
#     limit += 1

res = [0] * 7

max_res = [0] * 7
max_cost = 0
DFS(0, N)
print(max_cost)
print(*max_res)

