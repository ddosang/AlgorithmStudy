'''
곳감(모래시계)
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으
로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을
기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령
입니다.

1행 10 13 10 12 15     10 13 10 12 15
2행 12 39 30 23 11     23 11 12 39 30
3행 11 25 50 53 15     11 25 50 53 15
4행 19 27 29 37 27     19 27 29 37 27
5행 19 13 30 13 19     19 13 30 13 19

첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회
전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇
개가 있는지 출력하는 프로그램을 작성하세요.
'''


def rotateRow(row, leftAndRight, rotateCount):
    tempArr = arr[row]
    for i in range(rotateCount):
        if leftAndRight == 0:  # 왼쪽.
            right = tempArr.pop(0)
            tempArr.append(right)
        else:
            left = tempArr.pop(n - 1)
            tempArr.insert(0, left)

    arr[row] = tempArr


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

rotate = int(input())


for i in range(rotate):
    row, leftAndRight, rotateCount = map(int, input().split())
    rotateRow(row-1, leftAndRight, rotateCount)

total = 0
start = 0
end = n

for i in range(n):
    for j in range(start, end):
        total += arr[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
         start -= 1
         end += 1

#내 방식대로 푼다면
# total = 0
# mid = n // 2
# start = mid
# end = start + 1
#
# total += arr[mid][mid]
#
# while mid>0:
#     mid -= 1
#     start -= 1
#     end += 1
#
#     for i in range(start, end):
#         total += arr[mid][i]
#         total += arr[n-1-mid][i]

print(total)


'''
▣ 입력설명
첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령
정보가 M줄에 걸쳐 주어집니다.

▣ 출력설명
총 감의 개수를 출력합니다.
▣ 입력예제 1
5 1
0 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3 2
0 3
5 1 2
3 1 4
▣ 출력예제 1
362
'''