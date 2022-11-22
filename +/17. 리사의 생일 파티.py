import sys

readl = sys.stdin.readline

def price(cnt):
    # 해당 개수를 만들 수 있는 최소 금액
    if cnt <= 0:
        return 0

    sum = 0
    min_fee = 10

    for x, y, sm, pm, sv, pv in info:
        if sum > m:
            break

        필요한재료개수 = cnt * x - y

        if 필요한재료개수 <= 0:
            continue
        
        # 소매로 0개~소매최대개수까지.
        min_fee = 1000000000
        # print(cnt, (필요한재료개수 - 1) // sv + 1)
        for i in range((필요한재료개수 - 1) // sv + 2):
            도매개수 = i
            전체도매개수 = 도매개수 * sv

            소매개수 = 0
            if 필요한재료개수 - 전체도매개수 > 0:
                소매개수 = ((필요한재료개수 - 전체도매개수 - 1) // sm + 1)
            min_fee = min(min_fee, 소매개수 * pm + 도매개수 * pv)

        sum += min_fee if min_fee != 1000000000 else 0
    # print()
    
    # print(mid, sum)
    return sum



n, m = map(int, readl().split())
info = [list(map(int, readl().split())) for _ in range(n)]

# X : 한 식사를 완성하기 위해 필요한 양 (10<= X <=100)
# Y : 현재 주방에 준비되어 있는 양 (1<= Y <=100)
# Sm : 작은 포장에 담겨져 있는 재료의 양 (1 <= Sm <100)
# Pm : 작은 포장의 가격 (10<= Pm <100)
# Sv : 큰 포장에 담겨져 있는 재료의 양 (Sm < Sv <=100)
# Pv : 큰 포장의 가격 (Pm < Pv <=100)


left = 0
right = m

sol = -1

while left <= right:
    mid = (left + right) // 2

    # 가진 돈보다 해당 개수를 만족하는 돈이 적음. -> 개수 늘림.
    if price(mid) <= m:
        sol = mid
        left = mid + 1
    else:
        right = mid - 1
        
        

print(sol)