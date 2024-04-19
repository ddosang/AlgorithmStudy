n = int(input())
arr = []

for i in range(n):
    arr += [list(map(int, input().split()))]

m = int(input())
# 회전
for i in range(m):
    row, is_right, spin_count = map(int, input().split())
    row -= 1
    spin_count %= N # 240419 : N 번 돌면 다시 원점. 
    
    arr_row = arr[row]
    if is_right:
        arr_row = arr_row[n-spin_count:] + arr_row[:n-spin_count]
    else:
        arr_row = arr_row[spin_count:] + arr_row[:spin_count]

    arr[row] = arr_row

# 모래시계 영역 개수 세기
res = 0
count = 0
for i in range(n // 2):
    s = count
    e = n-1-count
    up = arr[i]
    down = arr[n-1-i]
    res += sum(up[s:e+1])
    res += sum(down[s:e+1])
    count += 1

if n % 2 == 1:
    res += arr[n//2][n//2]

print(res)
