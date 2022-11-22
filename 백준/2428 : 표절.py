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


    return sol + 1


n = int(readl())
files = list(map(int, readl().split()))

files.sort()

sum = 0

for i in range(1, n):
    start = leftLimit(i)
    sum += (i - start)


print(sum)