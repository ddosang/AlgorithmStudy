def solution(n):
    arr = sorted([int(c) for c in list(str(int(n)))], key=lambda x: -x)
    return int(''.join([str(i) for i in arr]))
