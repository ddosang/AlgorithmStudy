from collections import deque

n = int(input())
nums = list(map(int, input().split()))

nums = deque(nums)
count = 0
res = ""
last = 0


# 처음에 짠 건
# 왼쪽 오른쪽이 전부 마지막에 뽑은 것 보다 커야할 때만 신경씀.
# 한 쪽만 큰 걸 배제해서 답이 안나왔음.
while True:
    if nums[0] > last and nums[-1] > last:
        if nums[0] < nums[-1]:
            last = deque.popleft(nums)
            res += "L"
            count += 1
        else:
            last = deque.pop(nums)
            res += "R"
            count += 1
    elif nums[0] > last:
        last = deque.popleft(nums)
        res += "L"
        count += 1
    elif nums[-1] > last:
        last = deque.pop(nums)
        res += "R"
        count += 1
    else:
        break


print(count)
print(res)


# 강의 방법으로 복습
from functools import reduce

n = int(input())
numbers = list(map(int, input().split()))

lt = 0
rt = n-1
before = 0
l = []
res = []

while lt <= rt:
    if numbers[lt] > before:
        l.append((numbers[lt], "L"))
    if numbers[rt] > before:
        l.append((numbers[rt], "R"))

    if len(l) == 0:
        break
    
    l.sort()

    if before >= l[0][0]:
        break

    if l[0][1] == "L":
        lt += 1
    else:
        rt -= 1

    before = l[0][0]
    res.append(l[0])
    l.clear()


print(len(res))
print(reduce(lambda x, y: x + y, list(map(lambda x:x[1], res))))

