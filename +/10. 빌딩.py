import sys

readl = sys.stdin.readline

n = int(readl())

# 아 근데 당연히 시간초과 남..
# j = 0
# for i in range(1, n + 1):
#     # 4가 들어가면 안된다.
#     if '4' in str(i):
#         continue
#     j += 1
#
# print(j)


# 4라는 숫자가 하나 빠지는거니까 9진법이라고 생각하는데,
# [0, 1, 2, 3, 5, 6, 7, 8 ,9] 를 사용하는 9진.

def strangeNineToTen(n):
    # 4가 안돼서 바뀐거니까 그거부터 숫자 셋을 0~8로 바꿈.
    digit = [n if n < 4 else n - 1 for n in map(int, str(n))]
    
    # 그렇게 나온 9진을 10진으로
    sum = 0
    for d in digit:
        sum = sum * 9 + d
    return sum

print(strangeNineToTen(n))
