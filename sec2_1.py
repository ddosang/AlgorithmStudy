# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
K번째 약수
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
'''

import sys
#sys.stdin = open("input.txt", "rt")

n, k = input().split()

n = int(n)
k = int(k)


num = 0

for i in range(1, n+1):
    if n % i == 0: #나누어지면 약수임
        num += 1   #약수 개수 +1
    if num == k:   #k번째 약수라면
        print(i)   #출력 후 break
        break

if num < k:        #k가 약수의 개수보다 컸다면
    print(-1)      #-1 출력.
                   #if 대신 else를 써서 for-else문으로 쓸 수 있음.
                   #for-else: for문 정상 실행시 else 실행 X
                   #for문 중단 시 else 실행.

