n = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums

res = []
for i in range(n, 0, -1):
    res.insert(nums[i], i)

res = map(str, res)
print(' '.join(res))

