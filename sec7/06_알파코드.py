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


# 강의 코드
# index 체크, res 에 저장하는 부분 애초에 글자로 저장하도록 변형함

# 내가 한 건 글자를 한개씩 보면서 
# 0이 아니면 1자리 숫자로 바꿔보고
# 2자리 숫자로 바꿀 수 있으면 (26 이하면) 2자리로 바꾸고.
# 강의 코드는 알파벳을 기준으로 26개로 가지를 뻗어서 확인

strr = list(input())
N = len(strr)
res = [0] * N
cnt = 0

def DFS(level, index):
    global cnt
    if level == N:
        cnt += 1
        print(*res[:index], sep='')
        return
    
    for i in range(1, 27):
        if strr[level] == str(i):
            res[index] = chr(i + ord('A') - 1)
            DFS(level + 1, index + 1)
        elif level < N - 1 and i >= 10 and int(strr[level] + strr[level + 1]) == i:
            res[index] = chr(i + ord('A') - 1)
            DFS(level + 2, index + 1)


DFS(0, 0)
print(cnt)
