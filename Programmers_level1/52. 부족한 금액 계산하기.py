def solution(price, money, count):
    return sum([(i + 1) * price for i in range(count)]) - money
