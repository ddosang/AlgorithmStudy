# 개념만 듣고 풀었더니 파스칼 삼각형 식을...
# n! / (r! * (n-r)!) 으로 새우면.....? 매우 비효율적일 것 같아서 막혀있었다.

import sys

n, f = map(int, input().split())

def DFS(level):
    if level == n:
        local_sum = 0
        for i in range(n):
            local_sum += b[i] * res[i]

        if local_sum == f:
            for i in range(n):
                print(res[i], end=' ')
            sys.exit(0)

        return

    else:
        for i in range(1, n+1):
            if check[i] != 1:
                check[i] = 1
                res[level] = i
                DFS(level + 1)
                check[i] = 0


check = [0] * (n + 1)
b = [1] * n # 이항계수
res = [0] * n # 조합


# 수업에 나온 대박적 식 -> O(n)
for i in range(1, n - 1):
    b[i] = b[i - 1] * (n - i) / i


DFS(0)



# 수업 코드


import sys

n, f = map(int, input().split())

def DFS(level, sum): # sum 넘기는게 훨씬 깔끄.
    if sum > f:
        return

    if level == n 
        if sum == f:
            for i in range(n):
                print(res[i], end=' ')
            sys.exit(0)
        return

    else:
        for i in range(1, n+1):
            if check[i] != 1:
                check[i] = 1
                res[level] = i
                DFS(level + 1, sum + b[level] * res[level])
                check[i] = 0


check = [0] * (n + 1)
b = [1] * n # 이항계수
res = [0] * n # 조합


for i in range(1, n - 1):
    b[i] = b[i - 1] * (n - i) / i


DFS(0, 0)


# itertools permutations 사용

from itertools import permutations

n, f = map(int, input().split())
b = [1] * n

for i in range(1, n - 1):
    b[i] = b[i - 1] * (n - i) / i

arr = list(range(1, n + 1))


for p in permutations(arr, n):
    sum = 0
    for i in range(n):
        sum += b[i] * p[i]

    if sum == f:
        for i in range(n):
            print(p[i], end=' ')
        break


# 240627 복습
# 파스칼의 삼각형을 직접 더하기로 만듬 -> 더하기 횟수 O(n^2) 
import sys
input = sys.stdin.readline

# 2차원 배열에 N 줄의 파스칼 삼각형 채움
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# ...
def triangle(height):
    arr = [[0] * height for _ in range(height)]
    arr[0][0] = 1
    for row in range(1, height):
        arr[row][0] = 1
        arr[row][row] = 1
        for col in range(1, row):
            arr[row][col] = arr[row - 1][col - 1] + arr[row - 1][col]

    return arr

# 1차원 배열을 이용해서 위에서 N 줄에 저장했던 것을 N 줄에 저장하지 않고, 한줄에 계속 갱신
def triangle2(height):
    arr = [0] * N
    arr[0] = 1
    arr[1] = 1

    for row in range(2, height + 1):
        left = arr[0]
        right = arr[1]
        for col in range(1, row - 1):
            new = left + right
            left = right
            right = arr[col + 1]

            arr[col] = new
        arr[row - 1] = 1

    return arr
            

def DFS(level, current):
    if current > F:
        return

    if level == N:
        if current == F:
            print(*res, sep=' ')
            exit(0)

        return
    
    for i in range(1, N + 1):
        if ch[i] == 0:
            ch[i] = 1
            res[level] = i
            # DFS(level + 1, current + arr[N - 1][level] * i) # triangle 1
            DFS(level + 1, current + arr[level] * i)
            ch[i] = 0


# 파스칼의 삼각형
N, F = map(int, input().split())

ch = [0] * (N + 1)
res = [0] * N 

# arr = triangle(N)
arr = triangle2(N)
DFS(0, 0)

