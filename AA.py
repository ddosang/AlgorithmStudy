
import sys
sys.stdin = open("input.txt", "rt")

arr = [list(map(int, input().split())) for _  in range(7)]

n = 5
total = 0

#가로
for i in range(7): #행 7개
    for j in range(8-n): #이어지는 5글자는 7개 안에서 3개 나옴.
        check = []
        for k in range(n):
            check.append(arr[i][k + j])


        for k in range(n//2): #다섯 글자니까
            if arr[i][j+k] != arr[i][n-1-k+j]: #check 없이도 가능.
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
            if check[k] != check[n - 1 - k]:
                break  # 다른 숫자가 있으면 회문수가 아님.

        else:  # 이상 없이 돌아간다면 같은 숫자였다 -> 회문수
            total += 1

print(total)