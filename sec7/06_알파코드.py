strr = list(input())
N = len(strr)
res = []

def DFS(level, s):
    if level == N:
        res.append(s)
        return
    
    # 0은 10이나 20 에서 밖에 나올 수 없기 때문에
    # 0이 들어온다는건 앞에서 끊는걸 잘못했단거임.
    if int(strr[level]) == 0:
        return

    DFS(level + 1, s + chr(int(strr[level]) + ord('A') - 1))
    
    if level < N - 1:
        num = strr[level] + strr[level + 1]
        if int(num) <= 26:
            DFS(level + 2, s + chr(int(num) + ord('A') - 1))


DFS(0, "")
res.sort()
print(*res, sep='\n')
print(len(res))
