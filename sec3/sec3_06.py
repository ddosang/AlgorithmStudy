'''
격자판 최대합
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.
▣ 출력설명
최대합을 출력합니다.
▣ 입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
▣ 출력예제 1
155
'''


n = int(input())

arr = []
for _ in range(n):
    #arr += list(map(int, input().split())) #1차원
    arr.append(list(map(int, input().split()))) #2차원

#arr = [list(map(int, input().split())) for _ in range(n)]
#이렇게 읽어올 수 있음.

max = 0

#1차원으로 생각한 것
for i in range(n):
    total = 0
    #가로 합
    for j in range(n*i, n*(i+1)):
        total += arr[j]
    if max < total:
        max = total

    #세로합
    total = 0
    for j in range(i, n*n, n):
        total += arr[j]
    if max < total:
        max = total

#대각선합
total = 0
for j in range(0, n*n, n+1):
    total += arr[j]
if max < total:
    max = total

# 대각선합2
total = 0
for j in range(n - 1, n * n, n - 1):
    total += arr[j]
if max < total:
    max = total

max = 0

#2차원으로 생각한 것
for i in range(n):
    total = 0
    #가로 합
    for j in range(n):
        total += arr[i][j]
    if max < total:
        max = total


    #세로합
    total = 0
    for j in range(n):
        total += arr[j][i]
    if max < total:
        max = total


#대각선합1
total = 0
for i in range(n):
    total += arr[i][i]
    if max < total:
        max = total

#대각선합 2
total = 0
for i in range(n):
    total += arr[i][n-1-i]
    if max < total:
        max = total


print(max)
