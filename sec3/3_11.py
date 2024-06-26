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
    row = arr[i]
    for j in range(7-5+1):
        if check(row[j:j+5]):
            count += 1

# 세로
for i in range(7):
    for j in range((7-5+1)):
        # 이 부분 알고리즘은 바로 생각났는데 구현에서 꼬여서 푸는데 백년 걸렸다...
        end = j + 5
        for k in range(0, 2):
            if arr[j + k][i] != arr[end - 1 - k][i]:
                break
        else:
            count += 1

print(count)



# 240422
def check_palin(temp):
    length = len(temp) // 2

    for i in range(length):
        if temp[i] != temp[len(temp) - 1 - i]:
            return False
    
    return True

def check_palin_in_row(i):
    row = arr[i]
    
    cnt = 0
    leng = 5
    for i in range(len(row) - leng + 1):
        if check_palin(row[i:i+leng]):
            cnt += 1

    return cnt

def check_palin_in_col(i):
    col = []

    for j in range(7):
        col.append(arr[j][i])

    cnt = 0
    leng = 5
    for i in range(len(col) - leng + 1):
        if check_palin(col[i:i+leng]):
            cnt += 1
    
    return cnt


arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    cnt += check_palin_in_row(i)
    cnt += check_palin_in_col(i)

print(cnt)
