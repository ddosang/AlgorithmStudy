def solution(name):
    answer = 0
    
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        # 상하 이동
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
        next_i = i + 1
        while next_i < len(name) and name[next_i] == "A":
            next_i += 1
        
        # 좌우 이동
        min_move = min([min_move, 2 * i  + len(name) - next_i, 2 * (len(name) - next_i) + i])
    
    answer += min_move
    
    return answer
