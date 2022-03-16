def check(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n-1-i]:
            return False
    return True


count = 0
arr = []
for i in range(7):
    arr += [list(map(int, input().split()))]

# 가로
for i in range(7):
    if check(arr[i:i+5]):
        count += 1

# 세로
for i in range(7):
    for j in range((7-5+1)):
        flag = False
        for k in range(j, j+2):
            end = (2*j + 5)
            if arr[j][i] != arr[end - 1 - j][i]:
                break
        else:
            count += 1


print(count)
