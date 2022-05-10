# 개념만 듣고 풀었더니 파스칼 삼각형 식을...
# n! / r! 으로 새우면.....? 매우 비효율적일 것 같아서 막혀있었다.

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


# 수업에 나온 대박적 식
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
