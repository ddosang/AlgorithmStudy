# C언어 DFS 살짜쿵 보고 만듬. -> 그냥 한가지 경로만 찾는 것.
# 여러 경로를 찾아야하니까 DFS 에서 ch 를 이용해야한다.

def DFS(start):
    global cnt

    # 연결 그래프가 아니면 무한루프..
    if start == n - 1:
        cnt += 1
        return

    else:
        ch[start] = 1
        for i in range(n):
            if arr[start][i] == 1 and ch[i] == 0:
                res.append(i + 1)
                DFS(i)
                res.pop() # 경로 출력도 빼야함.
                ch[i] = 0 # 꺾는 것은 DFS 에서 방문한 곳 기준이니까.



n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]
ch = [0] * n

for i in range(m):
    start, end = map(int, input().split())
    arr[start - 1][end - 1] = 1

res = [1]
cnt = 0

DFS(0)
print(cnt)
