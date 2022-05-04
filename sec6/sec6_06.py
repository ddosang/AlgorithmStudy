# 혼자 짜다가 막혀서 설명을 들었는데,
# DFS(level + 1, i) 까지는 생각을 했는데,
# 그 결과를 저장해둘 생각을 못하고 있었던 거였다.
# 두개일 떄는 0 1 로 저장했으니까 여기는 1 2 3 ... n 을 저장하면 되는거였네.
# 그리고 그걸 출력하기만 하면 끝!

n, m = map(int, input().split())

def DFS(level, value):
    global count
    if level == m:
        for i in range(m):
            print(res[i], end=' ')
        count += 1
        print()

    else:
        for i in range(1, n+1):
            res[level] = i
            DFS(level + 1, i)


count = 0
res = [0] * (m)
DFS(0, 0)


print(count)


# 수업 코드

n, m = map(int, input().split())

def DFS(level):
    global count
    if level == m:
        for i in range(m):
            print(res[i], end=' ')
        count += 1
        print()

    else:
        for i in range(1, n+1):
            res[level] = i
            DFS(level + 1)


count = 0
res = [0] * (m)
DFS(0)

print(count)
