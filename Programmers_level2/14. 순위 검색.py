import re

def solution(info, query):
    answer = []
    
    info_split = []
    info_dict = {}
    
    # - 를 포함해서 모든 과목을 key 로 하는 dict 를 만든다.
    # 해당 key 를 가지는 사람의 점수 배열을 value 로 함.
    for l in ["java", "python", "cpp", "-"]:
        for j in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for f in ["pizza", "chicken", "-"]:
                    info_dict[l + j + c + f] = []
    
    # 모든 사람의 선택지를 만들어서 저장하되,
    # "-" 인 것에도 저장을 해줘야 함.
    for line in info:
        line = line.split(' ')
        for l in [line[0], "-"]:
            for j in [line[1], "-"]:
                for c in [line[2], "-"]:
                    for f in [line[3], "-"]:
                        info_dict[l + j + c + f].append(int(line[4]))
    
    
    # 점수 배열을 점수가 작은 것 부터 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

        
    for q in query:
        q = re.sub(" and ", "", q).split(' ')
        
        # 점수 배열 길이
        len_score = len(info_dict[q[0]])
        left = 0
        right = len_score - 1
        # 일단 점수 배열 개수를 index 로 하고,
        # index 에는 기준 점수와 같은 점수의 index 가 들어갈 것임. 
        # 만약 기준 점수와 같은 index 가 없으면 기준 점수보다 큰 것 중 가장 작은 것의 index
        index = len_score
        while left <= right:
            mid = (left + right) // 2
            if info_dict[q[0]][mid] >= int(q[1]):
                count = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # 큰 것의 개수가 필요한거니까 작은 것은 빼면 됨.
        # index 를 빼는거니까 + 1 은 할 필요 없음.
        answer.append(len(info_dict[q[0]]) - count)
    
    return answer
