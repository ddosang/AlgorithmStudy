'''
격자판 회문수
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
▣ 출력설명
5자리 회문수의 개수를 출력합니다.
▣ 입력예제 1
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1     -> 12321
1 3 1 3 5 3 2
1 1 2 5 6 5 2     -> 25652
1 2 2 2 2 1 5
    |
    22122
▣ 출력예제 1
3
'''
arr = [list(map(int, input().split())) for _  in range(7)]

n = 5
total = 0

#가로
for i in range(7): #행 7개
    for j in range(8-n): #이어지는 5글자는 7개 안에서 3개 나옴.
        check = []
        for k in range(n):
            check.append(arr[i][k + j])
        # 위의 3줄 대신
        # check = arr[i][j:j+5]

        for k in range(n//2): #다섯 글자니까
            # if arr[i][j+k] != arr[i][n-1-k+j]: #check 없이도 가능.
            if check[k] != check[n-1-k]:
                break #다른 숫자가 있으면 회문수가 아님.

        else: #이상 없이 돌아간다면 같은 숫자였다 -> 회문수
            total += 1

#세로
for i in range(7):  # 열 7개
    for j in range(8 - n):
        check = []
        for k in range(n):
            check.append(arr[k + j][i])

        for k in range(n // 2):  # 다섯 글자니까
            # if arr[j+k][i] != arr[n-1-k+j][i]: #check 없이도 가능.
            if check[k] != check[n - 1 - k]:
                break  # 다른 숫자가 있으면 회문수가 아님.

        else:  # 이상 없이 돌아간다면 같은 숫자였다 -> 회문수
            total += 1

print(total)