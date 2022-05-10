# 혼자 푼 것
n, m = map(int, input().split())

def DFS(level):
    global count

    if level == m:
        if not set(res) in total:
            count += 1
            for i in range(m):
                print(res[i], end=' ')
            print()

        total.append(set(res))

        return

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[level] = i
                DFS(level + 1)
                ch[i] = 0

count = 0
res = [0] * m
ch = [0] * (n + 1)
total = []

DFS(0)

print(count)


# 수업 코드
n, m = map(int, input().split())

def DFS(level, start):
    global count

    if level == m:
        count += 1
        for i in range(m):
            print(res[i], end=' ')
        print()

    else:
        for i in range(start, n+1):
            res[level] = i
            DFS(level + 1, i + 1)


count = 0
res = [0] * m
ch = [0] * (n + 1)

DFS(0, 1)

print(count)
