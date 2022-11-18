import sys

readl = sys.stdin.readline

n = int(readl())

도화지 = [[0] * 100 for _ in range(100)]

for _ in range(n):
    r, c = map(int, readl().split())
    r -= 1
    c -= 1
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            도화지[i][j] = 1


# 높이에 대한 누적합으로 색종이 붙인 곳을 채워두고
for i in range(1, 100):
    for j in range(100):
        if 도화지[i][j] == 1:
            도화지[i][j] = 도화지[i - 1][j] + 1


size = 0
max_size = 0

# 점 하나를 선택해서,
for row in range(100):
    for sw in range(100):
        if 도화지[row][sw] == 0:
            continue
        # 그 점부터 오른쪽으로 쭉 가면서 width 를 늘린다.
        height = 101

        for idx in range(sw, 100):
            # 그리고 해당 지점에 써있는 가장 작은 값이 height 가 됨.
            h = min(height, 도화지[row][idx])
            if height == 0:
                break
            size = height * (idx - sw + 1)
            max_size = max(max_size, size)

print(max_size)
