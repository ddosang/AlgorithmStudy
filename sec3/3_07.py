n = int(input())
arr = []

for i in range(n):
    arr += [list(map(int, input().split()))]

# 모래시계 영역 개수 세기
res = 0
count = 0
for i in range(n // 2):
    s = n//2 - count
    e = n//2 + count
    up = arr[i]
    down = arr[n-1-i]
    res += sum(up[s:e+1])
    res += sum(down[s:e+1])
    count += 1

if n % 2 == 1:
    res += arr[n//2][n//2]

print(res)


# 240419 복습
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

mid = N // 2
ans = 0
for i in range(mid):
    ans += sum(nums[i][mid - i:mid+i+1])
    ans += sum(nums[N - 1 - i][mid - i:mid+i+1])

ans += sum(nums[mid])

print(ans)
