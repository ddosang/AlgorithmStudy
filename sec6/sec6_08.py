# 혼자 푼 것
# 중복순열에서 한번 넣은 것을 안세면 될 것 같아서 check 를 이용하려고 했는데
# 장렬히 실패했다.

import sys
sys.stdin = open("input.txt")

def DFS(level):
    global count

    if level == m:
        for i in range(m):
            print(res[i], end=' ')
        count += 1
        print()

    else:
        check[level] = 1 # 체크를 했으니까 풀어야할텐데? 어디서...?
        for i in range(1, n+1):
            if check[i] != 1:
                res[level] = i
                DFS(level + 1)


n, m = map(int, input().split())
count = 0
check = [0] * (n + 1)
res = [0] * (m)

DFS(0)

print(count)



# 수업 코드

import sys
sys.stdin = open("input.txt")

def DFS(level):
    global count

    if level == m:
        for i in range(m):
            print(res[i], end=' ')
        count += 1
        print()

    else:
        for i in range(1, n+1):
            if check[i] != 1: # 아니라면
                check[i] = 1 # 사용했다고 체크!!!
                res[level] = i
                DFS(level + 1) # 하고 내려감!!!
                check[i] = 0 # 다시 돌아오면서 0 으로 바꿔서 다른 가지를 탈 수 있게


n, m = map(int, input().split())
count = 0
check = [0] * (n + 1)
res = [0] * (m)

DFS(0)

print(count)


# 240626 복습
# 이것보단 위의 방법이 나을듯. i in ch 를 체크하는데도 오래 걸림.
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
ch = [0] * M
cnt = 0

def H(level):
    global cnt
    if level == M:
        cnt += 1
        print(*ch, sep=' ')
        return
    
    for i in range(1, N + 1):
        if (not i in ch) and ch[level] == 0:
            ch[level] = i
            H(level + 1)
            ch[level] = 0


H(0)
print(cnt)

