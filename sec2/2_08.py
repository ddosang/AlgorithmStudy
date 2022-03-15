import math
def reverse(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
        res *= 10
    return res // 10

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    r = reverse(x)
    if isPrime(r):
        print(r, end=' ')
