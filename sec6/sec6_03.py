def DFS(v):
    if v == n+1:
        # 종료 조건.
        # 출력
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        check[v] = 1
        DFS(v + 1) # n + 1 까지 파고 들어가버리면 끝남.
        # 끝나고 다시 뒤돌아 나오는걸 표현하기 위해서
        # 위의 함수가 끝나면 v 를 0으로 바꿔서 사용하지 않는 쪽으로 뻗어나갈 수 있게 한다.
        check[v] = 0
        DFS(v + 1)


n = int(input())

vertexes = [i + 1 for i in range(n)]

check = [0] * (n + 1)
DFS(1)
