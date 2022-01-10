def solution(s):
    answer = ''
    arr = s.split(' ')
    for word in arr:
        for i in range(len(word)):
            answer += word[i].upper() if i % 2 == 0 else word[i].lower()
        answer += ' '
        
    answer = answer[:-1]
    
    return answer
