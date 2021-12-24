# https://programmers.co.kr/learn/courses/30/lessons/68935
def decimalToThreeReverse(n):
    res = ''
    while (n != 0):
        res += str(n % 3)
        n = int(n / 3)
        
    return int(res)

def threeToDecimal(n):
    res = 0
    power = 1
    while(n != 0):
        res += (n % 10) * power
        power *= 3
        n = int(n / 10)
        
    return res

def solution(n):
    return threeToDecimal(decimalToThreeReverse(n))
