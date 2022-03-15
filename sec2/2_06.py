def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x = x // 10

    return res


n = int(input())
arr = list(map(int, input().split()))
sum_arr = list(map(lambda x: digit_sum(x) ,arr))

print(arr[sum_arr.index(max(sum_arr))])
