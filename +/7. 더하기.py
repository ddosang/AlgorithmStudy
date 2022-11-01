import sys

def DFS(level, sum, start):
    global yes

    if level == N:
        if sum == K:
            yes = 1
            # print("YES")
        return

    if sum > K:
        return

    if sum == K:
        yes = 1
        # print("YES")
        return

    if sum < K:
        # start 도 따로 주면 앞의 것을 따로 저장해서 if 문 처리를 할 필요가 없는거였다.
        for i in range(start, N):
            res[level] = nums[i]
            DFS(level + 1, sum + nums[i], i + 1)


T = int(sys.stdin.readline())
for i in range(T):
    N, K = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    res = [0] * N

    yes = 0
    DFS(0, 0, 0)

    # if yes == 0:
        # print("NO")
    print("YES" if yes == 1 else "NO")
