import sys

readl = sys.stdin.readline


def 자릿수합(num):
    sum = 0

    while num > 0:
        sum += num % 10
        num //= 10

    return sum

def 숫자근(num):
    근 = 자릿수합(num)

    while 근 // 10:
        근 = 숫자근(근)

    return 근

n = int(readl())
nums = [int(readl()) for _ in range(n)]


roots = list(map(lambda x:숫자근(x), nums))
# print(roots)

# 근이 제일 큰거 찾아서 저장해두고
max_r = max(roots)
min_n = nums[roots.index(max_r)]

# 제일 큰 숫자근 가진 것 중에 제일 작은거
for idx, num in enumerate(nums):
    if max_r == roots[idx]:
        if min_n > num:
            min_n = num

print(min_n)
