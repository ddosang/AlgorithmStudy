# 1주차 2번 문제
# https://programmers.co.kr/learn/courses/30/lessons/81301

# 문자열을 넣어서 숫자 이름이면 숫자로 변환해주는 함수.
def change_string_to_num(s):
    if s == 'zero':
        return 0
    elif s == 'one':
        return 1
    elif s == 'two':
        return 2
    elif s == 'three':
        return 3
    elif s == 'four':
        return 4
    elif s == 'five':
        return 5
    elif s == 'six':
        return 6
    elif s == 'seven':
        return 7
    elif s == 'eight':
        return 8
    elif s == 'nine':
        return 9
    else:
        return 10


def solution(s):
    answer = 0
    local = ''

    # 들어온 문자열을 한 글자씩 읽는다.
    # 숫자라면 바로 숫자로 변환해서 뒤에 붙이고, 문자라면 해당 문자가 숫자의 이름일 때까지 읽은 후 숫자로 변환해서 붙인다.
    for c in s:
        if c.isdecimal():
            # 숫자 앞이 숫자 이름이었다면 해당 문자열도 문자로 변환해서 붙이고 넣어야함.
            if local != '':
                answer *= 10
                answer += change_string_to_num(local)
                local = ''

            answer *= 10
            answer += int(c)

        else:  # 문자라면
            local += c
            # 문자열이 숫자 이름이 될 때, 붙인다.
            if change_string_to_num(local) != 10:
                answer *= 10
                answer += change_string_to_num(local)
                local = ''

    # 만약 마지막이 문자열로 끝난다면, 마지막 숫자 이름을 붙여줘야 한다.
    if change_string_to_num(local) != 10:
        answer *= 10
        answer += change_string_to_num(local)

    return answer