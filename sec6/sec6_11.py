n, k = map(int, input().split())
arr = list(map(int, input().split()))
num = int(input())

def DFS(level, start, sum):
    global cnt

    if level == k:
        if sum % num == 0:
            cnt += 1

    else:
        for i in range(start, n):
            res[level] = arr[i]
            DFS(level + 1, i + 1, sum + arr[i])



res = [0] * k
cnt = 0

DFS(0, 0, 0)

print(cnt)
