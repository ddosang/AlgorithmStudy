# 비밀지도s
import re

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        res = arr1[i] | arr2[i] # or
        res = str(bin(res))[2:] # 0b 제거
        res = res if len(res) == n else ''.join(['0' for _ in range(n-len(res))]) + res # n자리가 아니면 n자리로 만들어줌
        # res = res if len(res) == n else ('0' * (n-len(res))) + res # 다시 풀었을 때 바뀐 부분.
        res = re.sub('1', '#', res) #정규표현식으로 1은 #
        res = re.sub('0', ' ', res) #0은 공백으로
        answer.append(res)
        
    return answers
