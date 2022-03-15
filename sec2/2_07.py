n = int(input())

cnt = 0
isPrime = [0] * (n+1)

# 2부터 가면서 해당 소수의 배수에 0을 저장하고,
# 또 0인걸 만나면 해당 알고리즘을 반복.
for i in range(2, n+1):
    if isPrime[i] == 0:
        cnt += 1
        # 해당 소수에도 1을 저장해도 되지만, 소수에 0을 저장하기 위해 2 * i 부터 시작했다.
        for j in range(2*i, n+1, i):
            isPrime[j] = 1

print(cnt)
