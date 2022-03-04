def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for c in s:
        if not c.isdigit(): #if ord(c) < 48 or 57 < ord(c):
            return False
    
    return True
