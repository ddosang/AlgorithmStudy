import re
def solution(s):
    s = s.lower()
    
    # p와 y를 각각 빼서 그 길이가 같으면 p, y 개수가 같은 것임.
    p = len(re.sub('p', '', s))
    y = len(re.sub('y', '', s))
    
    if p == y:
        return True

    return False
