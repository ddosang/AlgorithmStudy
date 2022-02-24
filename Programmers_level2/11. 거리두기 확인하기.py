import re

def solution(places):
    answer = []
    
    place_arr = []
    
    for place in places:
        # 1. 전체 배열에 P가 없는 경우는 거리두기를 지키고 있는 것
        if len(re.findall("P", ''.join(place))) == 0:
            answer.append(1)
            continue
            
        # 가생이는 따지기 귀찮으니까 X 로 채워주는 과정
        place_arr = [['X'] * (len(place) + 2)] 
        for row in place:
            place_arr.append(['X'] + list(row) + ['X'])
        place_arr.append(['X'] * (len(place) + 2))
        
            
        # 3. 세로와 대각선을 거르기 위한 나머지 경우에 대한 검사
        existNearPersons = False    
        for i in range(1, len(place) + 1):
            for j in range(1, len(place[0]) + 1):
                count = 0
                if place_arr[i][j] == "P" or place_arr[i][j] == "O":
                    if place_arr[i-1][j] == "P":
                        count += 1
                    if place_arr[i+1][j] == "P":
                        count += 1
                    if place_arr[i][j-1] == "P":
                        count += 1
                    if place_arr[i][j+1] == "P":
                        count += 1
                
                if place_arr[i][j] == "P" and count >= 1:
                    existNearPersons = True
                    break
                
                if place_arr[i][j] == "O" and count >= 2:
                    existNearPersons = True
                    break
                    
            if existNearPersons:
                answer.append(0)
                break
        else: ## if not existNearPersons: 와 같음
            answer.append(1)
                
    
    return answer
