import sys
from collections import deque
readl = sys.stdin.readline
    

def BFS(start):
    ch = [[[[10000] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]

    q = deque([(start, 0)])
    s1, s2, s3, s4 = start
    ch[s1][s2][s3][s4] = 1

    while q:
        num, cnt = q.popleft()

        # 바꾼게 목적지와 같으면.
        # 이거 검사 위치를 여기로 옮기니까 제대로 나옴.
        for i in range(4):
            if end[i] != num[i]:
                break
        else:
            return cnt

        # 천, 백, 십, 일 자리수를 탐색하기 위해서 4 이용.
        for i in range(4):

            # 해당 자릿수가 같으면 그걸 바꿀 필요는 없음.
            if num[i] == end[i]:
                continue

            # 해당 자릿수를 0~9 로 바꿔봄.
            for x in range(10):
                b1, b2, b3, b4 = num

                # 맨 앞자리가 0일수는 없으니까 뺌.
                if i == 0 and x == 0:
                    continue
                
                # x 가 바꿀 수랑 같은 수인 것도 검사할 필요 없음.
                if x == num[i]:
                    continue

                newnum = num[:i] + [x] + num[i + 1:]
                ncnt = cnt + 1

                n1, n2, n3, n4 = newnum

                if ch[n1][n2][n3][n4] != 10000:
                    continue

                # 숫자를 하나 바꿨는데 소수가 아니면
                if prime[int(''.join(map(str, newnum)))] == 0:
                    continue

                
                

                q.append((newnum, ncnt))
                ch[n1][n2][n3][n4] = ncnt
                # print(newnum)
    
    return -1


start, end = readl().rstrip().split()
start, end = list(map(int, start)), list(map(int, end))


# 소수 판정을 위해 소수 배열 채워둠.
prime = [1] * 10000
for i in range(2, 10000):
    if prime[i] == 1:
        for j in range(2 * i, 10000, i):
            prime[j] = 0

print(BFS(start))