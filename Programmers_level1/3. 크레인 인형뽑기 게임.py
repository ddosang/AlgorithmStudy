# 1주차 3번 문제
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stck = []

    for move in moves:
        for i in range(len(board)):
            # 하나의 열 안에서 움직이기 때문에 move 는 뒤에!
            item = board[i][move - 1]
            board[i][move - 1] = 0
            # 인형이 있는 곳까지 내려가서 뽑고 스택에 넣고 계산
            if item != 0:
                # 스택이 비어있으면 넣고
                if len(stck) == 0:
                    stck.append(item)
                # 비어있지 않으면
                else:
                    # 마지막 아이템과 같은지 확인하고 넣는다.
                    if stck[-1] == item:
                        stck.pop()
                        answer += 2
                    else:
                        stck.append(item)

                # 인형은 하나만 뽑으면 되니 break
                break

    return answer