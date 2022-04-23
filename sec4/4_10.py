n = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums

res = []
for i in range(n, -1, -1):
    res.insert(nums[i], i)

res = map(str, res)
print(' '.join(res))

# 강의방법 복습

n = int(input())
numbers = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if res[j] == 0:
            count += 1
        if count == numbers[i] + 1:
            res[j] = i + 1
            break
print(res)

# 강의 코드

n = int(input())
numbers = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    for j in range(n):
        if numbers[i] == 0 and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            numbers[i] -= 1

print(res)
