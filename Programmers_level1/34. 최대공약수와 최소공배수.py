def maX(n, m):
    if n < m:
        n, m = m, n
    if m == 0:
        return n
    
    return maX(m, n%m)
    

def solution(n, m):
    maXX = maX(n, m)
    return [maXX, n * m / maXX]
