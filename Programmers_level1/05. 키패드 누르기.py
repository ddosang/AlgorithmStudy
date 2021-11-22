# 어떤 손으로 선택할지 반환해주는 함수.
def which_hand(left_loca, right_loca, end, main_hand):
    # 거리가 짧은쪽을 반환하고
    if distance(left_loca, end) < distance(right_loca, end):
        return "L"
    elif distance(left_loca, end) > distance(right_loca, end):
        return "R"
    # 거리가 같으면, 주 사용 손을 반환.
    else:
        if main_hand == "left":
            return "L"
        else:
            return "R"

# 현재 위치와 눌러야 할 위치를 넣으면 거리를 계산해주는 함수.
def distance(start, end):
    # 1 2 3 이 x축 0 1 2 로
    # 1 4 7 이 y축 0 1 2 3 으로 맵핑.
    start_x = (start+2) % 3
    start_y = int((start - 1) / 3)
    
    end_x = (end+2) % 3
    end_y = int((end-1) / 3)
    
    # 거리가 칸 기준이므로 이렇게 거리를 구한다.
    dist = abs(start_x - end_x) + abs(start_y - end_y)
    return dist
    
    
def solution(numbers, hand):
    answer = ''
    left_loca = 10
    right_loca = 12
    
    for num in numbers:
        if num == 0:
            num = 11
        
        # 1, 4, 7 이면 left
        if num % 3 == 1:
            left_loca = num
            answer += "L"
        
        # 3, 6, 9 이면 right
        elif num % 3 == 0:
            right_loca = num
            answer += "R"
            
        # 2, 5, 8, 0 이면 계산 후에 결정.
        else:
            this_hand = which_hand(left_loca, right_loca, num, hand)
            # 손의 위치가 움직여야해서 아래 식도 추가.
            if this_hand == "L":
                left_loca = num
            else:
                right_loca = num
            answer += this_hand
    
    
    return answer
