def solution(x):
    sum = 0
    copyx = x
    
    while x > 0:
        sum += x % 10
        x = int(x/10)

    return True if copyx % sum == 0 else False


