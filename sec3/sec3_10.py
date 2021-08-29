'''
스토쿠 검사
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9
개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
예를 들어 다음을 보자.
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오
고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색
깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출
력하는 프로그램을 작성하세요.
'''

arr = [list(map(int, input().split())) for _ in range(9)]
oneToNine = list(range(10))
oneToNine.pop(0) #[1,2,3,4,5,6,7,8,9]를 만들어서 비교.

total = 0

for i in range(9):
    check = []
    for j in range(9): #가로 확인
        check.append(arr[i][j])

    check.sort()
    if check == oneToNine:
        total += 1
    else:
        break

    check.clear()
    for j in range(9): #세로
        check.append(arr[j][i])

    check.sort()
    if check == oneToNine:
        total += 1
    else:
        break


#네모들
for i in range(3):
    for j in range(3):
        check.clear()
        #작은 네모 하나.
        for k in range(3*i, 3*i+3):
            for l in range(3*j, 3*j+3):
                check.append(arr[k][l])

        check.sort()
        if check == oneToNine:
            total += 1
        else:
             break


if total == 27:
    print("YES")
else:
    print("NO")

#강의 방법: 배열을 입력으로 넣으면
# 전부 0으로 초기화 된 check 배열에
# check(arr[i][j]) = 1 로 있으면 체크를 해서
# sum(check) != 9 이면 false
# ==9 이면 True를 반환하는 함수 만들어 사용.


'''
▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.
'''