import sys

readl = sys.stdin.readline


def 자릿수제곱합(num):
    sum = 0
    while num:
        sum += (num % 10) ** 2
        num //= 10

    return sum

def isHappy(num):
    d = 자릿수제곱합(num)

    while True:
        d = 자릿수제곱합(d)

        # 행복한 수가 아니라면 자릿수제곱합은 언젠가 4가 나오는 성질이 있음.
        if d == 4:
            return False
        if d == 1:
            return True


n = int(readl())


print("HAPPY" if isHappy(n) else "UNHAPPY")

# for i in range(n, 0, -1):
#     if isHappy(i):
#         print(i)
#         break
