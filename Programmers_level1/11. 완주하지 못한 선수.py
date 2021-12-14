def solution(participant, completion):
    answer = ''

    count = 0
    dict = {}
    
    for person in participant:
        dict[person] = 0

    for person in participant:
        dict[person] += 1
    
    for completed_person in completion:
        dict[completed_person] -= 1
        
    for key in dict:
        if dict[key] == 1:
            answer = key
        
    
    return answer
