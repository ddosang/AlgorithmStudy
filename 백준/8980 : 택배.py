import sys

readl = sys.stdin.readline


n, c = map(int, readl().split())
m = int(readl())
post = [list(map(int, readl().split())) for _ in range(m)]

# # 어차피 c 보다 큰건 택배에 담을수도 없으니 줄여놓고 시작.
# post = list(map(lambda x: [int(x[0]), int(x[1]), int(x[2])] if int(x[2]) <= c else [int(x[0]), int(x[1]), c], post))
post.sort(key = lambda x:x[1])



res = 0
postman = [c] * (n + 1) # 마을별로 남아있는 무게

for s, e, w in post:
    min_left_weight = c
    # 짐이 해당 마을 구간 사이에서 계속 실려있을 수 있으려면
    # 남은 무게에서 가장 작은 만큼만 실을 수 있음.
    for i in range(s, e):
        min_left_weight = min(min_left_weight, postman[i])

    possible_weight = min(min_left_weight, w)
    for i in range(s, e):
        postman[i] -= possible_weight
    res += possible_weight

print(res)
