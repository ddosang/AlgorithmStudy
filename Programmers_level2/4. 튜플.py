# https://programmers.co.kr/learn/courses/30/lessons/64065
import re
def solution(s):
    arr = []
    arr2 = []
    answer = []
    
    # 맨 앞이랑 맨 뒤 {} 제거
    s = s[1:-1]
    
    # }, 로 나눠서 각 집합 기호를 하나씩 나눈다.
    # { } 를 제거하여 2 2,1 2,1,3 형식의 문자열을 arr에 넣음.
    for element in s.split('},'):
        nums = re.sub('{', '', element)
        nums = re.sub('}', '', nums)
        arr.append(nums)
    
    # 문자열 길이대로 정렬.
    # 긴 것에서 순서가 바뀌어도 되는 것을 고려해야하기 때문.
    arr = sorted(arr, key=lambda x:len(x))

    # ,로 split 해서 숫자로 바꾸고 arr2에 넣음.
    # 각 집합 원소가 한 행에 들어가는 2차원 배열이 됨.
    for x in arr:
        arr2.append(list(map(int, x.split(','))))
    
    # 해당 배열을 돌면서
    # 작은 것부터 배열에 넣는다.
    # 이미 있는 것은 넣지 않아도 됨.
    for i in range(len(arr2)):
        for y in arr2[i]:
            if not (y in answer):
                answer.append(y)
    
    return answer
