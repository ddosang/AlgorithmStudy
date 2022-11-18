import sys

readl = sys.stdin.readline

n = int(readl())
화학물질 = [list(map(int, readl().split())) for _ in range(n)]

화학물질.sort()

refridgelow, refridgehigh = 화학물질[0]
cnt = 1
for low, high in 화학물질:
    # 다음거 범위가 지금까지 쓴 냉장고 안에 들어울 수 있음.
    # 냉장고 범위를 더 좁게 갱신.
    if refridgelow <= low and high <= refridgehigh:
        refridgelow = low
        refridgehigh = high

    # 다음거가 이전거보다 높은 온도를 필요로 해서 냉장고에 들어올 수 없음.
    # 새로운 냉장고를 도입
    # sort 를 하고 시작하기 때문에 낮은 온도쪽은 비교할 필요가 없음.
    elif refridgehigh < low:
        refridgelow = low
        refridgehigh = high
        cnt += 1


print(cnt)
