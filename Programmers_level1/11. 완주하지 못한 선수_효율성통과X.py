def solution(participant, completion):
    answer = ''

    count = 0

    copy = participant

    for i in range(len(participant)-1, -1, -1):
        if len(completion) == 0:
            break
        if participant[i] in completion:
            completion.remove(participant[i])
            copy.pop(i)
            
    answer = copy[0]
    
    return answer
