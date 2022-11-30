import sys

readl = sys.stdin.readline

str = list(readl().strip())

balance = 0

open_cnt = 0
close_cnt = 0

for s in str:
    if s == "(":
        balance += 1
        open_cnt += 1
    else:
        balance -= 1
        close_cnt += 1
        # -1 이 됐다는건 지금까지의 앞에 ) 가 하나 더 있다는 뜻.
        if balance < 0:
            print(close_cnt)
            break

    # 닫힌게 더 많으면. 앞에 짝이 안맞는건 하나뿐이니까
    # 그 앞에 있는 닫힌걸 아무거나 뒤집어주면 됨.
    if balance < 0:
        sol = close_cnt

    # 열린게 더 많은데 1개 이하이면.
    # 이걸 바꿔버리면 balance 가 -1 이 되어버리므로, 뒤집으면 안됨.
    # 예를 들어서 ((() 에서 맨 앞에껀 뒤집을 수가 없음. 그 뒤에 있는 열린 괄호만 뒤집을 수 있음.
    # 2일때 바꿔서 balance 를 0 으로 맞춰야 함.
    if balance <= 1:
        open_cnt = 0
