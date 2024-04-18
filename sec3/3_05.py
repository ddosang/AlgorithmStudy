n, m = map(int, input().split())

arr = list(map(int, input().split()))

lt = 0
rt = 1
count = 0
sum_arr = arr[lt]

while rt <= n:
    sum_arr = sum(arr[lt:rt])
    if sum_arr == m:
        count += 1
        lt += 1
    elif sum_arr > m:
        lt += 1
    else:
        rt += 1

print(count)


# 240418
# sum 을 이용하지 않으면 while 문이 한번 돌 때 마다, 
# arr 의 하나의 요소에만 접근하면 됨.
N, M = map(int, input().split())
nums = list(map(int, input().split()))


cnt = 0
lt = 0
rt = 1
local_sum = nums[lt]
while lt < rt:
    if local_sum == M:
        cnt += 1
    
    if local_sum <= M and rt < N:
        local_sum += nums[rt]
        rt += 1
    else:
        local_sum -= nums[lt]
        lt += 1

print(cnt)
