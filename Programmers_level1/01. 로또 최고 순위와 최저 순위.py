# 1주차 1번 문제
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 순위 계산 함수.
# 6개 1등 5개 2등 ... 1개 이하로 맞으면 6등
def calculate_order(count):
    if count <= 1:
        return 6
    else:
        return 7 - count


def solution(lottos, win_nums):
    answer = []
    match_count = 0
    zero_count = 0
    high_order = 0
    low_order = 0

    # 먼저 맞은 번호 개수를 센다.
    for num in win_nums:
        for lotto in lottos:
            if num == lotto:
                match_count += 1

    # 모르는 번호의 개수를 샌다.
    for lotto in lottos:
        if lotto == 0:
            zero_count += 1

    # 모르는 번호도 다 맞았을 때가 순위가 가장 높다
    high_order = calculate_order(match_count + zero_count)
    # 모르는 번호가 다 틀리면 가장 낮은 순위.
    low_order = calculate_order(match_count)

    answer.append(high_order)
    answer.append(low_order)

    return answer