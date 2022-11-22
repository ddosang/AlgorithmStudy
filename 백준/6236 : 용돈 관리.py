import sys

readl = sys.stdin.readline


def spendMoney(fee):

    cur = 0
    cnt = 0

    for i, m in enumerate(money):
        # 만약에 충족이 안되면 가능한 수 중 큰 수를 내보내서 요금을 더 크게 만들어야함.
        if fee < m:
            return 10001

		# fee 보다 작으면 인출을 하고,
        if cur < m:
            cur = fee
            cnt += 1

		# 해당 금액을 쓴다.
        cur -= m

    return cnt


n, m = map(int, readl().split())
money = [int(readl()) for _ in range(n)]

# k >= sum(money) / m # 하루에 쓸 수 있는 평균 금액보다는 커야함.

start = max(money) # 91 % 에서 안넘어가서 당황했는데 이것때문이었다. 원래는 sum(money) // m 에서 시작함.
end = sum(money)
sol = 0

while start <= end:
    mid = (start + end) // 2

    # print(mid, spendMoney(mid))

    # 인출 횟수가 크면 금액을 높여야함.
    if spendMoney(mid) > m:
        start = mid + 1
    # 인출 횟수가 작거나 같으면 금액을 할수 있는 한 가장 작게
    else:
        end = mid - 1
        sol = mid

print(sol)