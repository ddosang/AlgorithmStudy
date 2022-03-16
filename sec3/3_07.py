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
