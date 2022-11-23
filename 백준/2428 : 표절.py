import sys

readl = sys.stdin.readline

# 넣은 숫자부터 0.9 ~ 1.0 사이에 있는 것을 다 검사하고,
def leftLimit(num):
    left = 0
    right = num - 1

    sol = -1

    while left <= right:
        mid = (left + right) // 2

        if files[mid] < 0.9 * files[num]:
            left = mid + 1
            sol = mid
        else:
            right = mid - 1

    # 0.9보다 작은것까지 찾은거니까
    # 그 다음꺼부터 검사해야함. +1
    return sol + 1


n = int(readl())
files = list(map(int, readl().split()))

files.sort()

sum = 0

for i in range(1, n):
    start = leftLimit(i)
    # 정렬된 배열에서 0.9 * files[i] 가 들어갈 가장 왼쪽 자리를 찾는다.
    # start = bisect.bisect_left(files, files[i] * 0.9, 0, i)
    sum += (i - start)


print(sum)