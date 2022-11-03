import sys

def dist(사대, 동물):
    return abs(동물[0] - 사대) + 동물[1]


readl = sys.stdin.readline

M, N, L = map(int, readl().split())
사대들 = list(map(int, readl().split()))
동물들 = [list(map(int, readl().split())) for _ in range(N)]

sum = 0


left = 0
right = M - 1

사대들.sort()

for 동물 in 동물들:
    left = 0
    right = M - 1

    while left <= right:
        mid = (left + right) // 2

        # 1
        if dist(사대들[mid], 동물) <= L:
            sum += 1
            break
        # 2
        elif 사대들[mid] <= 동물[0]:
            left = mid + 1
        # 3
        elif 사대들[mid] > 동물[0]:
            right = mid - 1


print(sum)
