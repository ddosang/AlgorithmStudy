import sys

readl = sys.stdin.readline

# 동 1 서 2 남 3 북 4

k = int(readl())

# 임의의 꼭짓점에서 도는 반시계 방향으로 주어짐.
arr = [list(map(int, readl().split())) for _ in range(6)]


# 넓이 = 가장큰세로 * 가장큰가로 - 빈부분세로 * 빈부분가로
# 가장 큰 가로와 가장 큰 세로를 찾자.
max_w = 0
max_w_idx = 0
max_h = 0
max_h_idx = 0

for idx, (direction, length) in enumerate(arr):
    if direction <= 2:
        if max_w < length:
            max_w = length
            max_w_idx = idx + 1
    if direction > 2:
        if max_h < length:
            max_h = length
            max_h_idx = idx + 1

# 빈부분을 찾기 위해서 max_w, max_h 를 찾은 것.
# max_w 에 붙어있는 세로 두개는 사용하는 세로이고, 붙어있지 않은 세로는 빈부분의 세로가 됨.
# 마찬가지로 max_h 에 붙은 가로 두개는 사용하는 가로이고, 붙지 않은 세로가 빈부분의 세로.
# 붙어있는 변은 어떻게 찾냐? 해당 변 기준으로 양 옆에 나오는지를 보면 됨.
# 그걸 위해서 맨 마지막거와 맨 첫번째거를 한번씩 더 패딩 (안하고 % 6 으로 해도 됨)
arr = [arr[-1]] + arr + [arr[0]]

빈부분세로 = abs(arr[(max_w_idx + 1)][1] - arr[(max_w_idx - 1)][1])
빈부분가로 = abs(arr[(max_h_idx + 1)][1] - arr[(max_h_idx - 1)][1])


넓이 = max_w * max_h - 빈부분세로 * 빈부분가로

print(k * 넓이)

