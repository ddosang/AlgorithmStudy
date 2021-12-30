def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    # 이전 월까지 날짜 + 주어진 날짜 를 7로 나눈 나머지로 요일 판별.
    JanFirst = 3 # 월요일이 0 이라 금요일은 4
    # 날짜 계산에서 이런 메커니즘을 쓰려면 (끝나는 날짜 - 시작 날짜) % 7 을 해야함.
    # 1월 1일은 빼야 계산을 할 수 있으므로 3
    sum = JanFirst + b
    
    for i in range(a):
        sum += month[i]

    return day[sum % 7]
